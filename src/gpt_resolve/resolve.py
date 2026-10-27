import asyncio
from pathlib import Path
from typing import Optional

import typer
from dotenv import load_dotenv

from gpt_resolve.pdf_generator import generate_solutions_pdf
from gpt_resolve.pipeline import (
    DEFAULT_JUDGE_MODEL,
    DEFAULT_MODEL,
    MAX_ROUNDS,
    PASS_SCORE,
    Settings,
    resolve_exam_async,
)
from gpt_resolve.providers import get_provider

# Load environment variables
load_dotenv(override=True)


def default_output_dir(source: Path, model: str) -> Path:
    """`prova.pdf` -> `prova_solutions/<model>`; image folder -> `<folder>/solutions/<model>`."""
    normalized_model_name = model.replace("-", "_").lower()
    if source.is_dir():
        return source / "solutions" / normalized_model_name
    return source.parent / f"{source.stem}_solutions" / normalized_model_name


def resolve_exam(
    source: Path,
    output_dir: Optional[Path] = None,
    questions_to_solve: Optional[list[int]] = None,
    provider_name: str = "claude",
    settings: Optional[Settings] = None,
):
    settings = settings or Settings()
    output_dir = output_dir or default_output_dir(source, settings.model)
    provider = get_provider(provider_name)
    return asyncio.run(
        resolve_exam_async(source, output_dir, provider, settings, questions_to_solve)
    ), output_dir


# Create Typer app
app = typer.Typer()


@app.command()
def resolve(
    path: Path = typer.Option(
        ..., "-p", "--path", help="Exam PDF, or a folder with q<n>.jpg images (+ conventions.jpg)"
    ),
    questions: Optional[str] = typer.Option(
        None, "-q", "--questions", help="Question numbers to solve separated by commas (e.g., 1,2,3)"
    ),
    output: Optional[Path] = typer.Option(None, "-o", "--output", help="Output folder for solutions"),
    provider: str = typer.Option("claude", help="Agent provider (claude, mock)"),
    model: str = typer.Option(DEFAULT_MODEL, "-m", "--model", help="Model for the solver agents"),
    judge_model: str = typer.Option(DEFAULT_JUDGE_MODEL, help="Model for the judge agents"),
    pass_score: float = typer.Option(PASS_SCORE, help="Minimum judge score (0-10) to approve"),
    max_rounds: int = typer.Option(MAX_ROUNDS, help="Max solve/judge rounds per question"),
    effort: str = typer.Option("high", help="Reasoning effort: low, medium, high, xhigh, max"),
    concurrency: int = typer.Option(4, help="Questions solved in parallel"),
    compile_pdf: bool = typer.Option(True, "--compile/--no-compile", help="Compile a PDF at the end"),
    title: str = typer.Option("Soluções", "-t", "--title", help="Title for the compiled PDF"),
    dry_run: bool = typer.Option(False, help="Use the offline mock provider"),
):
    """Resolve exam questions, each in its own agent, reviewed by an adversarial judge agent."""
    questions_list = [int(q) for q in questions.split(",")] if questions else None
    settings = Settings(
        model=model,
        judge_model=judge_model,
        pass_score=pass_score,
        max_rounds=max_rounds,
        effort=effort,
        concurrency=concurrency,
    )
    _, output_dir = resolve_exam(
        path, output, questions_list, "mock" if dry_run else provider, settings
    )
    if compile_pdf:
        generate_solutions_pdf(output_dir, title=title, author=f"{model} (solver) + {judge_model} (judge)")
        typer.echo(f"PDF: {output_dir}/solutions_compiled.pdf")


@app.command()
def compile_solutions(
    path: str = typer.Option(
        ..., "-p", "--path", help="Path to the folder containing the q<n>_solution.txt files"
    ),
    title: str = typer.Option("Solutions", "-t", "--title", help="Title for the PDF document"),
    author: str = typer.Option(DEFAULT_MODEL, "-a", "--author", help="Author of the solutions document"),
):
    """Compile all solutions from an exam directory into a single PDF document."""
    generate_solutions_pdf(path, title=title, author=author)
    typer.echo(f"Successfully generated PDF at {path}/solutions_compiled.pdf")


def main():
    app()


if __name__ == "__main__":
    app()
