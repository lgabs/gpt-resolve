"""Grade solutions against an external answer key: one agent per question compares both and points out doubts."""

import asyncio
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from gpt_resolve import prompts
from gpt_resolve.pipeline import Settings, run_agent

# An item counts as right for the solution when the grader says the solution (or both) is correct
CORRECT = ("solution", "both")
VERDICT_LABELS = {"match": "igual", "equivalent": "equivalente", "differs": "diferente", "not_answered": "não respondido"}


@dataclass
class KeyEntry:
    number: int
    answer: str
    resolution: str = ""
    url: str = ""


@dataclass
class AnswerKey:
    source: str
    entries: dict[int, KeyEntry]


@dataclass
class GradeResult:
    number: int
    grade: dict[str, Any]

    @property
    def items(self) -> list[dict[str, Any]]:
        return self.grade.get("items", [])

    @property
    def score(self) -> float:
        """Share of items where the solution is right, from 0 to 10."""
        if not self.items:
            return 0.0
        return 10 * sum(i["correct"] in CORRECT for i in self.items) / len(self.items)


def _as_text(value: Any) -> str:
    if isinstance(value, dict):
        return "\n".join(f"{k}) {v}" for k, v in value.items())
    return str(value or "")


def load_answer_key(path: Path) -> AnswerKey:
    """Read an answer key JSON: {"source": ..., "questions": [{"number", "answer", "resolution"?, "url"?}]}.
    `answer` may be a string or an object of answers per item (e.g. {"a": "...", "b": "..."})."""
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = {}
    for q in data["questions"]:
        entry = KeyEntry(int(q["number"]), _as_text(q["answer"]), _as_text(q.get("resolution")), q.get("url", ""))
        entries[entry.number] = entry
    return AnswerKey(data.get("source") or path.stem, entries)


def _load_questions(solutions_dir: Path) -> tuple[str, dict[int, dict[str, Any]]]:
    cache = solutions_dir / "questions.json"
    if not cache.exists():
        return "", {}
    data = json.loads(cache.read_text(encoding="utf-8"))
    return data.get("instructions", ""), {q["number"]: q for q in data["questions"]}


async def grade_question(
    number: int,
    key: AnswerKey,
    solutions_dir: Path,
    exam: Optional[Path],
    instructions: str,
    question: dict[str, Any],
    provider,
    settings: Settings,
    log=print,
) -> GradeResult:
    entry = key.entries[number]
    solution = (solutions_dir / f"q{number}_solution.txt").read_text(encoding="utf-8")
    judge_file = solutions_dir / f"q{number}_judge.json"
    final_answer = json.loads(judge_file.read_text(encoding="utf-8")).get("final_answer", "") if judge_file.exists() else ""
    sources = [str(exam.resolve())] if exam else []
    pages = question.get("pages", [])
    result = await run_agent(
        provider,
        settings,
        f"Q{number} gabarito",
        log,
        prompt=prompts.GRADER_PROMPT.format(
            number=number,
            key_source=key.source,
            sources=", ".join(sources) or "(indisponível, use a transcrição)",
            pages_hint=f" (páginas {', '.join(map(str, pages))})" if pages else "",
            instructions=instructions or "(nenhuma)",
            statement=question.get("statement", "(indisponível)"),
            solution=solution,
            final_answer=final_answer or "(veja a resolução)",
            key_answer=entry.answer,
            key_resolution=entry.resolution or "(não fornecida)",
        ),
        allowed_files=sources,
        system_prompt=prompts.GRADER_SYSTEM,
        model=settings.judge_model,
        workdir=solutions_dir / ".work" / f"q{number}" / "grade",
        schema=prompts.GRADER_SCHEMA,
        effort=settings.effort,
    )
    graded = GradeResult(number, result.structured)
    report = {"question": number, "key_source": key.source, "key_url": entry.url, "score": graded.score, **graded.grade}
    (solutions_dir / f"q{number}_grade.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"★ Q{number}: {graded.score:g}/10 pelo gabarito, {len(graded.grade.get('doubts', []))} ponto(s) de dúvida")
    return graded


def _cell(text: str) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def write_grade_report(results: list[GradeResult], key: AnswerKey, solutions_dir: Path) -> Path:
    """Summary in Markdown: score per question, item verdicts and the doubts to review."""
    total = sum(r.score for r in results) / len(results) if results else 0.0
    lines = [
        f"# Comparação com o gabarito: {key.source}",
        "",
        f"Nota média: **{total:.1f}/10** ({len(results)} questão(ões); cada item vale o mesmo dentro da questão).",
        "",
        "| Questão | Nota | Itens | Resumo |",
        "| ------- | ---- | ----- | ------ |",
    ]
    for r in results:
        verdicts = ", ".join(f"{i['item']}: {VERDICT_LABELS.get(i['verdict'], i['verdict'])}" for i in r.items)
        lines.append(f"| {r.number} | {r.score:.1f} | {_cell(verdicts)} | {_cell(r.grade.get('summary', ''))} |")
    lines += ["", "## Itens", ""]
    for r in results:
        lines += [f"### Questão {r.number}", "", "| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |", "| --- | --- | --- | --- | --- | --- |"]
        for i in r.items:
            lines.append(
                f"| {_cell(i['item'])} | {_cell(i['solution_answer'])} | {_cell(i['key_answer'])} | "
                f"{VERDICT_LABELS.get(i['verdict'], i['verdict'])} | {i['correct']} | {_cell(i['comment'])} |"
            )
        lines.append("")
    doubts = [(r.number, d) for r in results for d in r.grade.get("doubts", [])]
    # Doubts that may change an item's grade or reveal an error come first
    doubts.sort(key=lambda nd: nd[1].get("importance") != "high")
    lines += ["## Pontos de dúvida", ""]
    lines += [
        f"- **Q{n}** ({d['about']}{', importante' if d.get('importance') == 'high' else ''}): {_cell(d['description'])}"
        for n, d in doubts
    ] or ["Nenhum."]
    path = solutions_dir / "grade_report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


async def grade_exam_async(
    solutions_dir: Path,
    key_path: Path,
    provider,
    settings: Settings,
    exam: Optional[Path] = None,
    questions_to_grade: Optional[list[int]] = None,
    log=print,
) -> list[GradeResult]:
    start = time.perf_counter()
    base_log = log

    def log(msg: str) -> None:
        elapsed = int(time.perf_counter() - start)
        base_log(f"[{elapsed // 60:02d}:{elapsed % 60:02d}] {msg}")

    key = load_answer_key(key_path)
    instructions, questions = _load_questions(solutions_dir)
    numbers = sorted(
        n
        for n in key.entries
        if (solutions_dir / f"q{n}_solution.txt").exists() and (not questions_to_grade or n in questions_to_grade)
    )
    if not numbers:
        log(f"Nenhuma questão com resolução e gabarito em {solutions_dir}")
        return []
    log(f"{len(numbers)} questão(ões) para conferir contra {key.source}: {numbers}")

    semaphore = asyncio.Semaphore(settings.concurrency)

    async def run(n: int) -> Optional[GradeResult]:
        async with semaphore:
            try:
                return await grade_question(
                    n, key, solutions_dir, exam, instructions, questions.get(n, {}), provider, settings, log
                )
            except Exception as e:
                log(f"✗ Q{n} falhou: {type(e).__name__}: {str(e)[:200]} (rode de novo com -q {n})")
                return None

    results = [r for r in await asyncio.gather(*(run(n) for n in numbers)) if r]
    report = write_grade_report(results, key, solutions_dir)
    log(f"Concluído em {(time.perf_counter() - start) / 60:.1f} min. Custo estimado: US$ {settings.spent_usd:.2f}. Relatório: {report}")
    return results
