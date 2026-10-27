"""Exam pipeline: extract questions, then solve each one in its own agent with an adversarial judge loop."""

import asyncio
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from gpt_resolve import prompts
from gpt_resolve.providers import Provider
from gpt_resolve.utils import get_exam_images_paths

DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_JUDGE_MODEL = "claude-opus-5-5"
PASS_SCORE = 9.0
MAX_ROUNDS = 3


@dataclass
class Question:
    number: int
    statement: str
    sources: list[str]
    pages: list[int] = field(default_factory=list)


@dataclass
class Exam:
    instructions: str
    questions: list[Question]


@dataclass
class Attempt:
    round: int
    solution: str
    final_answer: str
    review: dict[str, Any]

    @property
    def score(self) -> float:
        return float(self.review.get("score", 0))


@dataclass
class QuestionResult:
    number: int
    attempts: list[Attempt]
    pass_score: float

    @property
    def best(self) -> Attempt:
        return max(self.attempts, key=lambda a: (a.score, a.round))

    @property
    def approved(self) -> bool:
        return self.best.score >= self.pass_score


@dataclass
class Settings:
    model: str = DEFAULT_MODEL
    judge_model: str = DEFAULT_JUDGE_MODEL
    pass_score: float = PASS_SCORE
    max_rounds: int = MAX_ROUNDS
    effort: Optional[str] = "high"
    concurrency: int = 4


def _pages_hint(question: Question) -> str:
    return f" (páginas {', '.join(map(str, question.pages))})" if question.pages else ""


async def load_exam(source: Path, provider: Provider, settings: Settings, output_dir: Path) -> Exam:
    """Build the exam from a PDF (extracted by an agent, cached in questions.json) or an image folder."""
    if source.is_dir():
        conventions, questions = get_exam_images_paths(str(source))
        sources = [str(Path(conventions).resolve())] if conventions else []
        return Exam(
            instructions="(veja a imagem de convenções, se houver)",
            questions=[
                Question(n, "(veja a imagem da questão)", sources + [str(Path(p).resolve())])
                for n, p in questions
            ],
        )

    cache = output_dir / "questions.json"
    if cache.exists():
        data = json.loads(cache.read_text(encoding="utf-8"))
    else:
        result = await provider.run(
            prompt=prompts.EXTRACT_PROMPT.format(sources=source.resolve()),
            system_prompt=prompts.EXTRACT_SYSTEM,
            model=settings.model,
            workdir=output_dir / ".work" / "extract",
            schema=prompts.EXTRACT_SCHEMA,
            effort="medium",
        )
        data = result.structured
        output_dir.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    return Exam(
        instructions=data.get("instructions", ""),
        questions=[
            Question(q["number"], q["statement"], [str(source.resolve())], q.get("pages", []))
            for q in data["questions"]
        ],
    )


def _format_feedback(review: dict[str, Any]) -> str:
    lines = [review.get("summary", "")]
    for issue in review.get("issues", []):
        lines.append(f"- [{issue['severity']}] {issue['description']}")
    return "\n".join(lines)


async def solve_question(
    question: Question, exam: Exam, provider: Provider, settings: Settings, output_dir: Path, log=print
) -> QuestionResult:
    """Solve one question; while the judge scores below the pass score, revise with its feedback."""
    workdir = output_dir / ".work" / f"q{question.number}"
    common = dict(
        number=question.number,
        sources=", ".join(question.sources),
        pages_hint=_pages_hint(question),
        instructions=exam.instructions or "(nenhuma)",
        statement=question.statement,
    )
    attempts: list[Attempt] = []
    for round_ in range(1, settings.max_rounds + 1):
        revision = ""
        if attempts:
            last = attempts[-1]
            revision = prompts.REVISION_BLOCK.format(
                score=last.score, previous=last.solution, feedback=_format_feedback(last.review)
            )
        solved = await provider.run(
            prompt=prompts.SOLVER_PROMPT.format(**common, revision=revision),
            system_prompt=prompts.SOLVER_SYSTEM,
            model=settings.model,
            workdir=workdir / "solver",
            schema=prompts.SOLVER_SCHEMA,
            effort=settings.effort,
        )
        solution = solved.structured["solution_latex"]
        judged = await provider.run(
            prompt=prompts.JUDGE_PROMPT.format(**common, solution=solution),
            system_prompt=prompts.JUDGE_SYSTEM,
            model=settings.judge_model,
            workdir=workdir / "judge",
            schema=prompts.JUDGE_SCHEMA,
            effort=settings.effort,
        )
        attempt = Attempt(round_, solution, solved.structured.get("final_answer", ""), judged.structured)
        attempts.append(attempt)
        log(f"Q{question.number} rodada {round_}: nota {attempt.score:g}")
        if attempt.score >= settings.pass_score:
            break

    result = QuestionResult(question.number, attempts, settings.pass_score)
    save_result(result, output_dir)
    return result


def save_result(result: QuestionResult, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    best = result.best
    header = f"\\section*{{Questão {result.number}}}"
    (output_dir / f"q{result.number}_solution.txt").write_text(
        header + "\n\n" + best.solution, encoding="utf-8"
    )
    report = {
        "question": result.number,
        "approved": result.approved,
        "pass_score": result.pass_score,
        "best_round": best.round,
        "score": best.score,
        "final_answer": best.final_answer,
        "rounds": [
            {"round": a.round, "score": a.score, "final_answer": a.final_answer, "review": a.review}
            for a in result.attempts
        ],
    }
    (output_dir / f"q{result.number}_judge.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    for a in result.attempts:
        (output_dir / ".work" / f"q{result.number}").mkdir(parents=True, exist_ok=True)
        (output_dir / ".work" / f"q{result.number}" / f"round{a.round}_solution.txt").write_text(
            a.solution, encoding="utf-8"
        )


async def resolve_exam_async(
    source: Path,
    output_dir: Path,
    provider: Provider,
    settings: Settings,
    questions_to_solve: Optional[list[int]] = None,
    log=print,
) -> list[QuestionResult]:
    start = time.perf_counter()
    exam = await load_exam(source, provider, settings, output_dir)
    questions = [q for q in exam.questions if not questions_to_solve or q.number in questions_to_solve]
    log(f"{len(questions)} questão(ões) para resolver: {[q.number for q in questions]}")

    semaphore = asyncio.Semaphore(settings.concurrency)

    async def run(q: Question) -> QuestionResult:
        async with semaphore:
            return await solve_question(q, exam, provider, settings, output_dir, log)

    results = sorted(await asyncio.gather(*(run(q) for q in questions)), key=lambda r: r.number)
    for r in results:
        status = "aprovada" if r.approved else "NÃO aprovada"
        log(f"Q{r.number}: nota {r.best.score:g} ({status}, {len(r.attempts)} rodada(s))")
    log(f"Concluído em {(time.perf_counter() - start) / 60:.1f} min. Saída: {output_dir}")
    return results
