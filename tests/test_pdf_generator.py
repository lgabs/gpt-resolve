import pytest
from gpt_resolve.pdf_generator import generate_solutions_pdf


def test_generate_solutions_pdf(tmp_path):
    # Create mock solutions directory
    solutions_dir = tmp_path / "solutions"
    solutions_dir.mkdir()

    # Create mock solution file
    solution_file = solutions_dir / "q1_solution.txt"
    solution_file.write_text(
        r"""
    \section*{Question 1}
    This is a test solution.
    """
    )

    # Generate PDF
    generate_solutions_pdf(tmp_path, "Test Exam")

    # Check if PDF was created
    assert (tmp_path / "solutions/solutions_compiled.pdf").exists()


def test_generate_solutions_pdf_no_dir():
    with pytest.raises(FileNotFoundError):
        generate_solutions_pdf("nonexistent_path", "Test Exam")
