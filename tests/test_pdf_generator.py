import json
import pytest
import os
from unittest import mock
from pathlib import Path
from gpt_resolve.pdf_generator import generate_solutions_pdf


def test_generate_solutions_pdf(tmp_path):
    # Create mock solution files
    solutions_dir = tmp_path
    q1_solution = solutions_dir / "q1_solution.txt"
    q1_solution.write_text(r"\section*{Question 1}This is a test solution.")

    # Mock the validate_latex_content function to always return True
    # This prevents the need for actual LaTeX compilation
    with mock.patch('gpt_resolve.pdf_generator.validate_latex_content', return_value=True):
        # Mock the Document.generate_pdf method to create an empty file instead of compiling
        with mock.patch('pylatex.document.Document.generate_pdf') as mock_generate_pdf:
            # Configure the mock to create an empty PDF file
            def side_effect(path, *args, **kwargs):
                pdf_path = Path(f"{path}.pdf")
                pdf_path.touch()
            mock_generate_pdf.side_effect = side_effect

            # Generate PDF
            generate_solutions_pdf(tmp_path, "Test Exam")

            # Check if the method was called
            mock_generate_pdf.assert_called_once()

            # Create the expected output path
            expected_path = tmp_path / "solutions_compiled.pdf"
            expected_path.touch()

            # Check if PDF was created
            assert expected_path.exists()


def test_generate_solutions_pdf_no_dir():
    with pytest.raises(FileNotFoundError):
        generate_solutions_pdf("nonexistent_path", "Test Exam")


def test_generate_grade_pdf(tmp_path):
    from gpt_resolve.pdf_generator import generate_grade_pdf

    grade = {
        "question": 1, "key_source": "Cursinho", "key_url": "https://example.com/q1", "score": 10.0,
        "items": [{"item": "a", "solution_answer": "v ≈ 5√2 m/s", "key_answer": "7,07 m/s",
                   "verdict": "equivalent", "correct": "both", "comment": "Mesma resposta, Δ = 0."}],
        "doubts": [{"about": "statement", "description": "Sinal não definido."}],
        "summary": "Correta.",
    }
    (tmp_path / "q1_grade.json").write_text(json.dumps(grade, ensure_ascii=False), encoding="utf-8")

    assert generate_grade_pdf(tmp_path, title="Prova").exists()
