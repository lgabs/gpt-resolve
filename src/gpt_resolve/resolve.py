import time
import base64

from dotenv import load_dotenv
import typer
from typing import Optional, List

from openai import OpenAI
from tqdm import tqdm

from gpt_resolve.utils import get_exam_images_paths, save_answer_and_description
from gpt_resolve.pdf_generator import generate_solutions_pdf

MAX_COMPLETION_TOKENS = 10_000
DEFAULT_MODEL = "o1"

# Initialize OpenAI client as a global variable
load_dotenv(override=True)
OPENAI_CLIENT = OpenAI()

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def resolve_question(
    question_image: str,
    conventions_image: str,
    model: str = DEFAULT_MODEL,
    max_tokens_output: int = MAX_COMPLETION_TOKENS,
    dry_run: bool = False,
    client: OpenAI = OPENAI_CLIENT,
) -> tuple[str, int]:
    """Resolves the given question with an OpenAI pipeline directly passing images to the specified model."""
    if dry_run:
        return (
            "\\section*{Solução}\\n\\nMock solution for testing purposes.\\n\\nANSWER: 42",
            200,
        )

    response = client.responses.create(
        model=model,
        max_output_tokens=max_tokens_output,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Você é um especialista de exames de admissão universitária."
                            "Resolva o problema mostrado nas imagens a seguir."
                            "Responda à questão de forma clara e objetiva, explicando o raciocínio passo a passo, mas seja objetivo, "
                            "como se estivesse resolvendo a questão em uma prova de vestibular, com espaço de no máximo uma página para a resposta."
                            "Use a notação LaTeX para sua resposta, inclusive para fórmulas, equações ou destacar palavras em negrito ou itálico."
                            "Sua resposta deve compreender apenas uma seção na sintaxe do LaTeX, começando com \section*{Solução}."
                            "Quando usar `align*`, não coloque-o dentro dos delimitadores `\[` e `\]`. Exemplo de uso: \begin{align*}x^2+1\end{align*}"
                            "Use vírgulas para separação decimal e não use pontos para separação de milhares."
                            "Indique a solução final com um 'ANSWER:' seguido do resultado."
                        ),
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{conventions_image}"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{question_image}",
                    },
                ],
            }
        ],
    )

    answer = response.output_text
    total_tokens = response.usage.total_tokens

    return answer, total_tokens


def process_questions(
    questions_images: list[tuple[int, str]],
    conventions_image: str,
    exam_path: str,
    dry_run: bool,
    max_tokens_output: int,
    model: str = DEFAULT_MODEL,
) -> None:
    """Processes the given questions using the OpenAI client by directly passing images to the specified model."""
    total_questions = len(questions_images)
    print(
        f"Starting to process {total_questions} questions. Each question can take a while to process when using reasoning models."
    )

    start_time = time.perf_counter()

    for idx, (question_num, question_image) in enumerate(questions_images):
        pbar = tqdm(
            total=total_questions,
            desc=f"Processing Question {question_num}",
            position=idx,
            leave=True,
            unit="question",
            initial=idx,
        )

        # Process the question directly with specified model
        answer, total_tokens = resolve_question(
            question_image=question_image,
            conventions_image=conventions_image,
            model=model,
            dry_run=dry_run,
            max_tokens_output=max_tokens_output,
            client=OPENAI_CLIENT,
        )

        pbar.set_postfix({"Total Tokens": total_tokens})

        # Generate an empty placeholder for question_description since we're no longer extracting it
        # but the save function still expects it
        question_description = f"\\section*{{Questão {question_num}}}"

        save_answer_and_description(
            answer, question_description, exam_path, question_num, model, dry_run=dry_run
        )
        pbar.update(1)
        pbar.close()

    end_time = time.perf_counter()
    total_time = end_time - start_time

    total_minutes = total_time / 60
    print(f"All questions processed successfully in {total_minutes:.2f} minutes.")


def resolve_exam(
    exam_path: str,
    questions_to_solve: list[int] = None,
    dry_run: bool = False,
    max_tokens_output: int = MAX_COMPLETION_TOKENS,
    model: str = DEFAULT_MODEL,
) -> None:
    """
    Resolves the given exam with GPT up to `questions_to_solve` questions.
    If `questions_to_solve` is not provided, all questions will be solved.
    """

    conventions_path, questions_paths = get_exam_images_paths(exam_path)
    if questions_to_solve:
        questions_paths = [
            (q, p) for q, p in questions_paths if q in questions_to_solve
        ]

    # Encode the images
    conventions_image: str = encode_image(conventions_path)
    questions_images: list[tuple[int, str]] = [
        (i, encode_image(question_path)) for i, question_path in questions_paths
    ]

    # Process the questions using the encapsulated function
    process_questions(
        questions_images=questions_images,
        conventions_image=conventions_image,
        exam_path=exam_path,
        dry_run=dry_run,
        max_tokens_output=max_tokens_output,
        model=model,
    )


# Create Typer app
app = typer.Typer()


@app.command()
def resolve(
    path: str = typer.Option(..., "-p", "--path", help="Path to the exam directory"),
    questions: Optional[str] = typer.Option(
        None,
        "-q",
        "--questions",
        help="Question numbers to solve separated by commas (e.g., 1,2,3)",
    ),
    dry_run: bool = typer.Option(
        False, help="Run in dry-run mode without making actual API calls"
    ),
    max_tokens_output: int = typer.Option(
        MAX_COMPLETION_TOKENS, help="Maximum output tokens"
    ),
    model: str = typer.Option(
        "o1", "-m", "--model", help="OpenAI model to use for generating solutions"
    ),
):
    """Resolve exam questions using GPT."""
    questions_list = [int(q) for q in questions.split(",")] if questions else None
    resolve_exam(
        exam_path=path,
        questions_to_solve=questions_list,
        dry_run=dry_run,
        max_tokens_output=max_tokens_output,
        model=model,
    )


@app.command()
def compile_solutions(
    path: str = typer.Option(
        ...,
        "-p",
        "--path",
        help="Path to the exam directory containing a solutions folder",
    ),
    title: str = typer.Option(
        "Solutions", "-t", "--title", help="Title for the PDF document"
    ),
    author: str = typer.Option(
        "o1-preview (OpenAI)", "-a", "--author", help="Author of the solutions document"
    ),
):
    """Compile all solutions from an exam directory into a single PDF document."""
    generate_solutions_pdf(path, title=title, author=author)
    typer.echo(f"Successfully generated PDF at {path}/solutions_compiled.pdf")


def main():
    app()


if __name__ == "__main__":
    app()
