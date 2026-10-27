from pathlib import Path
from typing import Union
from pylatex import Document, Command
from pylatex.utils import NoEscape, escape_latex
import datetime
import tempfile
import subprocess
import json
from pylatex import Itemize

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
    exam_path: Union[str, Path], title: str, author="gpt-resolve"
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

    sol_files_with_issues = []
    # Add each solution to document; a solution with broken LaTeX is reported, not fatal
    for sol_file in solution_files:
        content = sol_file.read_text(encoding="utf-8")
        if not validate_latex_content(content):
            sol_files_with_issues.append(str(sol_file))
            doc.append(NoEscape(f"\\section*{{{sol_file.stem}}}"))
            doc.append(f"Solution has invalid LaTeX, see {sol_file.name}.")
        else:
            doc.append(NoEscape(content))
        doc.append(NoEscape(r"\newpage"))

    judge_reports = sorted(
        solutions_dir.glob("q*_judge.json"), key=lambda x: int(x.stem.split("_")[0][1:])
    )
    if judge_reports:
        append_judge_appendix(doc, judge_reports)

    # Generate PDF in the exam directory. pdflatex runs in nonstop mode, so a PDF is usually
    # produced even when it reports errors; only fail if there is no PDF at all.
    output = exam_path / "solutions_compiled"
    try:
        doc.generate_pdf(str(output), clean_tex=False)
    except Exception as e:
        if not output.with_suffix(".pdf").exists():
            raise
        print(f"Warning: LaTeX reported errors, check {output}.log ({type(e).__name__})")

    if sol_files_with_issues:
        print(
            "Warning: invalid LaTeX in:\n"
            + "\n".join(sol_files_with_issues)
            + "\nRe-run those questions with -q or fix them manually."
        )


def append_judge_appendix(doc: Document, judge_reports: list[Path]) -> None:
    """Add the judge's score and review for each question as an appendix."""
    doc.append(NoEscape(r"\section*{Apêndice: parecer do avaliador}"))
    for report_file in judge_reports:
        report = json.loads(report_file.read_text(encoding="utf-8"))
        status = "aprovada" if report["approved"] else "não aprovada"
        review = report["rounds"][report["best_round"] - 1]["review"]
        doc.append(
            NoEscape(
                f"\\subsection*{{Questão {report['question']}: nota "
                f"{str(report['score']).replace('.', ',')} ({status}, "
                f"rodada {report['best_round']} de {len(report['rounds'])})}}"
            )
        )
        doc.append(NoEscape(escape_text(review.get("summary", ""))))
        issues = review.get("issues", [])
        if issues:
            with doc.create(Itemize()) as itemize:
                for issue in issues:
                    itemize.add_item(
                        NoEscape(escape_text(f"[{issue['severity']}] {issue['description']}"))
                    )


# Unicode symbols the judge tends to write in plain text, which pdflatex can't typeset as-is
UNICODE_TO_LATEX = {
    "−": "-", "–": "--", "—": "---", "≈": r"$\approx$", "≤": r"$\leq$", "≥": r"$\geq$",
    "≠": r"$\neq$", "→": r"$\to$", "⇒": r"$\Rightarrow$", "⇔": r"$\Leftrightarrow$",
    "×": r"$\times$", "·": r"$\cdot$", "√": r"$\sqrt{}$", "∞": r"$\infty$", "∈": r"$\in$",
    "±": r"$\pm$", "°": r"$^\circ$", "²": r"$^2$", "³": r"$^3$", "½": r"$\frac12$",
    "Δ": r"$\Delta$", "∆": r"$\Delta$", "Ω": r"$\Omega$", "Σ": r"$\Sigma$", "Π": r"$\Pi$",
    "∫": r"$\int$", "∑": r"$\sum$", "∂": r"$\partial$", "∠": r"$\angle$", "≡": r"$\equiv$",
    "ℝ": r"$\mathbb{R}$", "ℂ": r"$\mathbb{C}$", "ℕ": r"$\mathbb{N}$", "ℤ": r"$\mathbb{Z}$",
}
GREEK = "αβγδεζηθικλμνξπρστυφχψω"
GREEK_NAMES = ["alpha", "beta", "gamma", "delta", "varepsilon", "zeta", "eta", "theta", "iota",
               "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma", "tau", "upsilon",
               "varphi", "chi", "psi", "omega"]
UNICODE_TO_LATEX.update({c: f"$\\{n}$" for c, n in zip(GREEK, GREEK_NAMES)})


def escape_text(text: str) -> str:
    """Escape plain text for LaTeX, mapping common math symbols and dropping other non-Latin-1 chars."""
    escaped = escape_latex(text)
    out = []
    for ch in escaped:
        if ch in UNICODE_TO_LATEX:
            out.append(UNICODE_TO_LATEX[ch])
        elif ord(ch) > 255:
            out.append("?")
        else:
            out.append(ch)
    return "".join(out)
