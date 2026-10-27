import asyncio
import json

from gpt_resolve.pipeline import Settings, resolve_exam_async
from gpt_resolve.providers import get_provider
from gpt_resolve.providers.mock import MockProvider
from gpt_resolve.resolve import default_output_dir


def run(source, output_dir, provider, settings=None, questions=None):
    return asyncio.run(
        resolve_exam_async(
            source, output_dir, provider, settings or Settings(), questions, log=lambda *_: None
        )
    )


def test_pdf_exam_extracts_and_caches_questions(tmp_path):
    pdf = tmp_path / "prova.pdf"
    pdf.touch()
    out = tmp_path / "out"
    provider = MockProvider(num_questions=3)

    results = run(pdf, out, provider, questions=[1, 3])

    assert [r.number for r in results] == [1, 3]
    assert provider.calls.count("extract") == 1
    assert (out / "questions.json").exists()
    assert (out / "q1_solution.txt").read_text(encoding="utf-8").startswith("\\section*{Questão 1}")
    assert not (out / "q2_solution.txt").exists()

    # Second run reuses the cached extraction
    run(pdf, out, provider, questions=[2])
    assert provider.calls.count("extract") == 1


def test_judge_loop_revises_until_pass_score(tmp_path):
    pdf = tmp_path / "prova.pdf"
    pdf.touch()
    provider = MockProvider(judge_scores=[6, 8.5, 9.2], num_questions=1)

    (result,) = run(pdf, tmp_path / "out", provider)

    assert [a.score for a in result.attempts] == [6, 8.5, 9.2]
    assert result.approved
    report = json.loads((tmp_path / "out" / "q1_judge.json").read_text(encoding="utf-8"))
    assert report["approved"] and report["best_round"] == 3


def test_judge_loop_stops_at_max_rounds_and_keeps_best(tmp_path):
    pdf = tmp_path / "prova.pdf"
    pdf.touch()
    provider = MockProvider(judge_scores=[7, 8.5, 5], num_questions=1)

    (result,) = run(pdf, tmp_path / "out", provider, Settings(max_rounds=3))

    assert len(result.attempts) == 3
    assert not result.approved
    assert result.best.round == 2


def test_image_folder_exam_skips_extraction(temp_exam_dir, tmp_path):
    provider = MockProvider()

    results = run(temp_exam_dir, tmp_path / "out", provider, questions=[2])

    assert [r.number for r in results] == [2]
    assert "extract" not in provider.calls


def test_default_output_dir(tmp_path):
    pdf = tmp_path / "prova.pdf"
    pdf.touch()
    assert default_output_dir(pdf, "claude-opus-5-5") == tmp_path / "prova_solutions" / "claude_opus_5_5"
    assert default_output_dir(tmp_path, "x") == tmp_path / "solutions" / "x"


def test_get_provider():
    assert get_provider("mock").name == "mock"
    assert get_provider("claude").name == "claude"
