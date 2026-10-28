import asyncio
import json

from gpt_resolve.grading import grade_exam_async, load_answer_key
from gpt_resolve.pipeline import Settings
from gpt_resolve.providers.mock import MockProvider


def write_key(path, questions):
    path.write_text(json.dumps({"source": "Cursinho", "questions": questions}), encoding="utf-8")


def test_load_answer_key_accepts_text_or_items(tmp_path):
    key_path = tmp_path / "key.json"
    write_key(key_path, [{"number": 1, "answer": {"a": "10 m", "b": "2 s"}}, {"number": 2, "answer": "42", "url": "u"}])

    key = load_answer_key(key_path)

    assert key.source == "Cursinho"
    assert key.entries[1].answer == "a) 10 m\nb) 2 s"
    assert key.entries[2].url == "u"


def test_grade_writes_reports_for_solved_questions(tmp_path):
    out = tmp_path / "solutions"
    out.mkdir()
    for n in (1, 2):
        (out / f"q{n}_solution.txt").write_text("Solução", encoding="utf-8")
    key_path = tmp_path / "key.json"
    write_key(key_path, [{"number": n, "answer": "42"} for n in (1, 2, 3)])
    provider = MockProvider()

    results = asyncio.run(grade_exam_async(out, key_path, provider, Settings(), log=lambda *_: None))

    # Q3 has no solution, so only Q1 and Q2 are graded
    assert [r.number for r in results] == [1, 2]
    assert provider.calls.count("grade") == 2
    grade = json.loads((out / "q1_grade.json").read_text(encoding="utf-8"))
    assert grade["score"] == 5 and grade["key_source"] == "Cursinho"
    report = (out / "grade_report.md").read_text(encoding="utf-8")
    assert "Nota média: **5.0/10**" in report
    assert "**Q1** (key, importante): Mock doubt." in report
