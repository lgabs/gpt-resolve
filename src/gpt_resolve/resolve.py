import os
import time
import base64
import argparse
from dotenv import load_dotenv

from openai import OpenAI
from tqdm import tqdm

from gpt_resolve.utils import get_exam_images_paths, save_answer_and_description

MAX_TOKENS_QUESTION_DESCRIPTION = 400  # for gpt-4o
MAX_COMPLETION_TOKENS = 5000  # for o1-preview, much higher tokens are needed


def get_openai_client():
    """Initialize OpenAI client with API key from environment variables."""
    load_dotenv(override=True)
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def extract_question_description(
    client: OpenAI, question_image: str, conventions_image: str, dry_run: bool = False
) -> tuple[str, int]:
    """Extracts the question description from the given question image."""
    if dry_run:
        time.sleep(5)
        return (
            "\\section*{Questão 1}\\n\\nMock question description for testing purposes.",
            100,
        )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Extraia o enunciado da questão e as alternativas, se existirem."
                            "Caso haja imagens, descreva-as de forma clara e objetiva de forma que seja possível entender o problema sem a necessidade de ver a imagem."
                            "Use apenas notação LaTeX, inclusive para fórmulas, equações ou destacar palavras em negrito ou itálico."
                            "Sua resposta deve compreender apenas uma seção na sintaxe do LaTeX, começando com \section*{Questão N}, sem nada antes ou depois."
                            "Exemplo de enunciado: \section*{Questão 1}\n\nEnunciado da questão 1."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{conventions_image}"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{question_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=MAX_TOKENS_QUESTION_DESCRIPTION,
    )
    description = response.choices[0].message.content
    total_tokens = response.usage.total_tokens

    return description, total_tokens


def resolve_question(
    client: OpenAI,
    question_description: str,
    max_completion_tokens: int = MAX_COMPLETION_TOKENS,
    dry_run: bool = False,
) -> tuple[str, int]:
    """Resolves the given question with an OpenAI pipeline using gpt-4o to describe the question and o1-preview to solve it."""
    if dry_run:
        return (
            "\\section*{Solução}\\n\\nMock solution for testing purposes.\\n\\nANSWER: 42",
            200,
        )

    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Você é um especialista de exames de admissão universitária."
                            "Resolva o problema indicado entre os delimitadores ```."
                            "Responda à questão de forma clara e objetiva, explicando o raciocínio passo a passo, mas seja objetivo."
                            "Use a notação LaTeX para sua resposta, inclusive para fórmulas, equações ou destacar palavras em negrito ou itálico."
                            "Sua resposta deve compreender apenas uma seção na sintaxe do LaTeX, começando com \section*{Solução}."
                            "Indique a solução final com um 'ANSWER:' seguido do resultado."
                            f"O enunciado da questão é:```{question_description}```"
                        ),
                    },
                ],
            }
        ],
        max_completion_tokens=max_completion_tokens,
    )
    answer = response.choices[0].message.content
    total_tokens = response.usage.total_tokens

    return answer, total_tokens


def process_questions(
    questions_images: list[tuple[int, str]],
    conventions_image: str,
    exam_path: str,
    dry_run: bool = False,
) -> None:
    """Processes the given questions using the OpenAI client."""
    client = get_openai_client()
    total_questions = len(questions_images)
    for idx, (question_num, question_image) in enumerate(questions_images):
        pbar = tqdm(
            total=total_questions,
            desc=f"Processing Question {question_num}",
            position=idx,
            leave=True,
            unit="question",
            initial=idx,
        )
        # Process the question
        question_description, total_tokens_desc = extract_question_description(
            client, question_image, conventions_image, dry_run=dry_run
        )

        answer, total_tokens_ans = resolve_question(
            client, question_description, dry_run=dry_run
        )
        pbar.set_postfix(
            {"Desc Tokens": total_tokens_desc, "Ans Tokens": total_tokens_ans}
        )
        save_answer_and_description(
            answer, question_description, exam_path, question_num, dry_run=dry_run
        )
        pbar.update(1)
        pbar.close()
    print("All questions processed successfully.")


def resolve_exam(
    exam_path: str, questions_to_solve: list[int] = None, dry_run: bool = False
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
    )


def main():
    parser = argparse.ArgumentParser(
        description="Resolve exam questions using GPT-4o and o1-preview",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Examples:
                gpt-resolve -p exams/ita_2025/math/essays
                gpt-resolve -p exams/ita_2025/math/essays -q 1 2 3
                gpt-resolve -p exams/ita_2025/math/essays --dry-run
        """,
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=True,
        help="Path to the exam directory (e.g., 'exams/ita_2025/math/essays')",
    )
    parser.add_argument(
        "-q",
        "--questions",
        type=lambda x: [int(i) for i in x.split(",")],
        help="Question numbers to solve (e.g., 1 or 1,2,3). If not provided, all questions will be solved",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run in dry-run mode without making actual API calls",
    )

    args = parser.parse_args()

    resolve_exam(
        exam_path=args.path, questions_to_solve=args.questions, dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
