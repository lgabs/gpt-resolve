from pathlib import Path
from typing import Union
from pylatex import Document, Command
from pylatex.utils import NoEscape
import datetime
import tempfile
import subprocess

def compile_solution(content: str) -> bool:
    """
    Compile a LaTeX document to check if the content has valid LaTeX syntax.

    Args:
        content (str): The LaTeX content to check.

    Returns:
        bool: True if compilation is successful, False otherwise.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_file = Path(temp_dir) / "temp_solution.tex"
        doc = Document()
        doc.append(NoEscape(content))
        doc.generate_tex(str(tex_file))
        try:
            result = subprocess.run(
                ["pdflatex", "-output-directory", temp_dir, tex_file],
                capture_output=True, text=True
            )
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
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
    solutions_dir = exam_path / "solutions"

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

    # Validate each solution before adding to the document
    for sol_file in solution_files:
        print(f"Validating solution: {sol_file.name}")
        content = sol_file.read_text(encoding="utf-8")
        
        if not compile_solution(content):
            print(f"Error: Solution '{sol_file.name}' has LaTeX syntax errors. Please fix it.")
            return 

    print("All solutions are valid. Generating the final PDF...")

    # Add each solution to document
    for sol_file in solution_files:
        content = sol_file.read_text(encoding="utf-8")
        doc.append(NoEscape(content))
        doc.append(NoEscape(r"\newpage"))

    # Generate PDF in the exam directory
    doc.generate_pdf(str(exam_path / "solutions/solutions_compiled"), clean_tex=True)
