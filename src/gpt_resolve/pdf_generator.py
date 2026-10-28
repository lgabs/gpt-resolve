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
        reference = report.get("judge_reference")
        if reference:
            doc.append(
                NoEscape(
                    r"\textbf{Resposta da resolução às cegas do avaliador:} "
                    + escape_text(reference.get("final_answer", ""))
                    + r"\par "
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
    "×": r"$\times$", "·": r"$\cdot$", "√": r"$\surd$", "∞": r"$\infty$", "∈": r"$\in$",
    "±": r"$\pm$", "°": r"$^\circ$", "²": r"$^2$", "³": r"$^3$", "½": r"$\frac12$",
    "Δ": r"$\Delta$", "∆": r"$\Delta$", "Ω": r"$\Omega$", "Σ": r"$\Sigma$", "Π": r"$\Pi$",
    "∫": r"$\int$", "∑": r"$\sum$", "∂": r"$\partial$", "∠": r"$\angle$", "≡": r"$\equiv$",
    "ℝ": r"$\mathbb{R}$", "ℂ": r"$\mathbb{C}$", "ℕ": r"$\mathbb{N}$", "ℤ": r"$\mathbb{Z}$",
    "≅": r"$\cong$", "∝": r"$\propto$", "∓": r"$\mp$", "…": r"\ldots{}", "Ṡ": r"$\dot S$",
    "Ẇ": r"$\dot W$", "ẑ": r"$\hat z$", "ŷ": r"$\hat y$", "\u0307": "",
}
UNICODE_TO_LATEX.update({c: f"$^{{{d}}}$" for c, d in zip("⁰¹⁴⁵⁶⁷⁸⁹⁻", "01456789-")})
UNICODE_TO_LATEX.update({c: f"$_{{{d}}}$" for c, d in zip("₀₁₂₃₄₅₆₇₈₉", "0123456789")})
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


VERDICTS = {"match": "igual", "equivalent": "equivalente", "differs": "diferente", "not_answered": "não respondido"}
CORRECT_LABELS = {"solution": "resolução", "key": "gabarito", "both": "ambos", "neither": "nenhum", "unclear": "indefinido"}


def generate_grade_pdf(solutions_dir: Union[str, Path], title: str) -> Path:
    """Compile the q<n>_grade.json files into grade_report.pdf: scores, item verdicts and doubts."""
    solutions_dir = Path(solutions_dir)
    grades = [
        json.loads(f.read_text(encoding="utf-8"))
        for f in sorted(solutions_dir.glob("q*_grade.json"), key=lambda x: int(x.stem.split("_")[0][1:]))
    ]
    if not grades:
        raise FileNotFoundError(f"No q<n>_grade.json files in {solutions_dir}")
    key_source = escape_text(grades[0].get("key_source", ""))
    total = sum(g["score"] for g in grades) / len(grades)
    items = [i for g in grades for i in g["items"]]
    right = sum(i["correct"] in ("solution", "both") for i in items)

    doc = Document(geometry_options={"margin": "2.2cm"})
    for pkg in ["amsmath", "amssymb", "booktabs", "longtable", "array", "hyperref"]:
        doc.preamble.append(Command("usepackage", pkg))
    doc.preamble.append(Command("hypersetup", "hidelinks"))
    doc.preamble.append(
        Command(
            "title",
            NoEscape(
                f"{escape_text(title)}\\\\[4pt]\\large Comparação com o gabarito {key_source}"
                "\\thanks{Gerado com gpt-resolve: \\url{https://github.com/lgabs/gpt-resolve}}"
            ),
        )
    )
    doc.preamble.append(Command("date", datetime.datetime.now().strftime("%d/%m/%Y")))
    doc.append(NoEscape(r"\maketitle"))
    def num(x: float) -> str:
        return f"{x:.1f}".replace(".", ",")

    doc.append(
        NoEscape(
            f"\\section*{{Resumo}}\\textbf{{Nota média: {num(total)}/10}} ({right} de {len(items)} itens com a resolução "
            "correta; cada item vale o mesmo dentro da questão).\\par\\medskip"
        )
    )
    rows = [
        f"{g['question']} & {num(g['score'])} & {escape_text(g.get('summary', ''))} \\\\"
        for g in grades
    ]
    doc.append(
        NoEscape(
            "\\begin{longtable}{@{}c c p{0.78\\textwidth}@{}}\\toprule Questão & Nota & Resumo \\\\ \\midrule\n"
            + "\n".join(rows)
            + "\n\\bottomrule\\end{longtable}"
        )
    )
    main_doubts = [(g["question"], d) for g in grades for d in g.get("doubts", []) if d.get("importance") == "high"]
    if main_doubts:
        doc.append(NoEscape(r"\section*{Principais pontos de dúvida}"))
        with doc.create(Itemize()) as itemize:
            for n, d in main_doubts:
                itemize.add_item(NoEscape(f"\\textbf{{Q{n}}} \\textit{{({escape_text(d['about'])})}} " + escape_text(d["description"])))
    for g in grades:
        doc.append(NoEscape(f"\\section*{{Questão {g['question']}}}"))
        if g.get("key_url"):
            doc.append(NoEscape(f"\\href{{{g['key_url']}}}{{Resolução do gabarito}}\\par\\smallskip"))
        rows = [
            f"{escape_text(i['item'])} & {escape_text(i['solution_answer'])} & {escape_text(i['key_answer'])} & "
            f"{VERDICTS.get(i['verdict'], i['verdict'])} & {CORRECT_LABELS.get(i['correct'], i['correct'])} \\\\"
            for i in g["items"]
        ]
        doc.append(
            NoEscape(
                "\\begin{longtable}{@{}p{0.06\\textwidth} p{0.33\\textwidth} p{0.33\\textwidth} p{0.1\\textwidth} p{0.08\\textwidth}@{}}"
                "\\toprule Item & Resolução & Gabarito & Veredito & Certo \\\\ \\midrule\n"
                + "\n".join(rows)
                + "\n\\bottomrule\\end{longtable}"
            )
        )
        comments = [i for i in g["items"] if i.get("comment")]
        if comments:
            with doc.create(Itemize()) as itemize:
                for i in comments:
                    itemize.add_item(NoEscape(f"\\textbf{{{escape_text(i['item'])})}} " + escape_text(i["comment"])))
        if g.get("doubts"):
            doc.append(NoEscape(r"\paragraph{Pontos de dúvida}"))
            with doc.create(Itemize()) as itemize:
                for d in g["doubts"]:
                    itemize.add_item(NoEscape(f"\\textit{{({escape_text(d['about'])})}} " + escape_text(d["description"])))

    output = solutions_dir / "grade_report"
    try:
        doc.generate_pdf(str(output), clean_tex=False)
    except Exception as e:
        if not output.with_suffix(".pdf").exists():
            raise
        print(f"Warning: LaTeX reported errors, check {output}.log ({type(e).__name__})")
    return output.with_suffix(".pdf")
