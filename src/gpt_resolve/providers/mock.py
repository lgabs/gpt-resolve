"""Offline provider for --dry-run and tests."""

from pathlib import Path
from typing import Any, Optional

from gpt_resolve.providers.base import AgentResult, Provider


class MockProvider(Provider):
    name = "mock"

    def __init__(self, judge_scores: Optional[list[float]] = None, num_questions: int = 2):
        self.judge_scores = list(judge_scores or [9.5])
        self.num_questions = num_questions
        self.calls: list[str] = []

    async def run(
        self,
        *,
        prompt: str,
        system_prompt: str,
        model: str,
        workdir: Path,
        schema: Optional[dict[str, Any]] = None,
        effort: Optional[str] = None,
        max_turns: Optional[int] = None,
    ) -> AgentResult:
        props = (schema or {}).get("properties", {})
        if "questions" in props:
            self.calls.append("extract")
            questions = [
                {"number": n, "pages": [n], "statement": f"Enunciado da questão {n}."}
                for n in range(1, self.num_questions + 1)
            ]
            return AgentResult("", {"instructions": "", "questions": questions})
        if "reference_solution" in props:
            self.calls.append("blind")
            return AgentResult(
                "", {"reference_solution": "Mock reference.", "final_answer": "42", "pitfalls": []}
            )
        if "score" in props:
            self.calls.append("judge")
            score = self.judge_scores.pop(0) if len(self.judge_scores) > 1 else self.judge_scores[0]
            return AgentResult(
                "",
                {
                    "score": score,
                    "answer_correct": True,
                    "agrees_with_reference": True,
                    "issues": [] if score >= 9 else [{"severity": "major", "description": "Passo sem justificativa."}],
                    "summary": f"Mock review, nota {score}.",
                },
            )
        self.calls.append("solve")
        return AgentResult(
            "",
            {"solution_latex": "\\section*{Solução}\n\nMock solution.\n\nANSWER: 42", "final_answer": "42"},
        )
