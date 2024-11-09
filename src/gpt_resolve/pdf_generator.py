from pathlib import Path
from pylatex import Document, Section, Command
from pylatex.utils import NoEscape
import datetime


def generate_solutions_pdf(
    exam_path: str | Path, title: str, author="o1-preview (OpenAI)"
) -> None:
    """
    Generate a PDF document containing all solutions from an exam directory.

    Args:
        exam_path: Path to the exam directory containing a solutions folder
    """
    exam_path = Path(exam_path)
    solutions_dir = exam_path / "solutions"

    if not solutions_dir.exists():
        raise FileNotFoundError(f"Solutions directory not found at {solutions_dir}")

    # Create document
    doc = Document()

    # Add preamble
    doc.preamble.append(Command("usepackage", "amsmath"))
    doc.preamble.append(Command("usepackage", "amssymb"))
    doc.preamble.append(Command("usepackage", "amsfonts"))
    doc.preamble.append(Command("usepackage", "graphicx"))
    doc.preamble.append(Command("usepackage", "hyperref"))
    doc.preamble.append(
        Command(
            "title",
            NoEscape(
                f"{title}\\thanks{{Made with gpt-resolve: \\url{{https://github.com/lgabs/gpt-resolve}}}}"
            ),
        )
    )
    doc.preamble.append(Command("author", author))
    doc.preamble.append(Command("date", datetime.datetime.now().strftime("%B %d, %Y")))
    doc.append(NoEscape(r"\maketitle"))

    # Get all solution files sorted
    solution_files = sorted(solutions_dir.glob("*_solution.txt"))

    # Add each solution to document
    for sol_file in solution_files:
        content = sol_file.read_text(encoding="utf-8")
        doc.append(NoEscape(content))

        doc.append(NoEscape(r"\newpage"))

    # Generate PDF in the exam directory
    doc.generate_pdf(str(exam_path / "solutions/solutions_compiled"), clean_tex=True)
