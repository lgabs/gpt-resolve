from pathlib import Path
from typing import Union
from pylatex import Document, Command
from pylatex.utils import NoEscape
import datetime
import tempfile
import subprocess

def validate_latex_content(content: str) -> bool:
    """
    Validate a LaTeX document by attempting to compile it, checking for syntax validity.

    Args:
        content (str): The LaTeX content to check.

    Returns:
        bool: True if compilation is successful, False otherwise.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_file = Path(temp_dir) / "temp_solution"
        doc = Document()

        # Add required packages for validation
        packages = [
            "amsmath",
            "amssymb",
            "amsfonts",
            "graphicx",
            "hyperref",
            "tikz",
            "pgfplots",
        ]
        for pkg in packages:
            doc.preamble.append(Command("usepackage", pkg))

        tikz_libraries = ["math"]
        for lib in tikz_libraries:
            doc.preamble.append(Command("usetikzlibrary", lib))

        doc.append(NoEscape(content))
        try:
            # Attempt to compile the LaTeX document to PDF
            doc.generate_pdf(str(tex_file), clean_tex=True)
            return True
        except Exception as e:
            print(f"Error compiling LaTeX content: {e}")
            return False


def generate_solutions_pdf(
    exam_path: Union[str, Path], title: str, author="o1-preview (OpenAI)"
) -> None:
    """
    Generate a PDF document containing all solutions from an exam directory.

    Args:
        exam_path: Path to the exam directory containing a solutions folder
    """
    exam_path = Path(exam_path)
    solutions_dir = exam_path

    if not solutions_dir.exists():
        raise FileNotFoundError(f"Solutions directory not found at {solutions_dir}")

    # Create document
    doc = Document()

    # Add preamble
    packages = [
        "amsmath",
        "amssymb",
        "amsfonts",
        "graphicx",
        "hyperref",
        "tikz",
        "pgfplots",
    ]
    for pkg in packages:
        doc.preamble.append(Command("usepackage", pkg))

    tikz_libraries = [
        "math",
    ]
    for lib in tikz_libraries:
        doc.preamble.append(Command("usetikzlibrary", lib))

    doc.preamble.append(
        Command(
            "title",
            NoEscape(
                f"{title}\\thanks{{This exam was solved and automatically generated with gpt-resolve: \\url{{https://github.com/lgabs/gpt-resolve}}}}"
            ),
        )
    )
    doc.preamble.append(Command("author", author))
    doc.preamble.append(Command("date", datetime.datetime.now().strftime("%B %d, %Y")))
    doc.append(NoEscape(r"\maketitle"))

    # Get all solution files sorted
    solution_files = sorted(
        solutions_dir.glob("*_solution.txt"),
        key=lambda x: int(x.stem.split("_")[0][1:]),
    )
        # Get all solution files sorted
    solution_files = sorted(
        solutions_dir.glob("*_solution.txt"),
        key=lambda x: int(x.stem.split("_")[0][1:])
    )

    sol_files_with_issues = []
    # Add each solution to document
    for sol_file in solution_files:
        content = sol_file.read_text(encoding="utf-8")
        if not validate_latex_content(content):
            sol_files_with_issues.append(str(sol_file))
            continue
        doc.append(NoEscape(content))
        doc.append(NoEscape(r"\newpage"))

    if sol_files_with_issues:
        raise ValueError(
            "Errors in one or more solutions:\n"
            + "\n".join(sol_files_with_issues)
            + "\n\nPlease check for syntax errors."
        )

    # Generate PDF in the exam directory
    doc.generate_pdf(str(exam_path / "solutions_compiled"), clean_tex=True)
