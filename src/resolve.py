import os
import base64

from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

from src.utils import get_exam_images_paths, save_answer_and_description

# Load environment variables from .env file
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

MAX_TOKENS_QUESTION_DESCRIPTION = 400 # for gpt-4o
MAX_COMPLETION_TOKENS = 5000 # for o1-preview, much higher tokens are needed


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def extract_question_description(
    question_image: str, conventions_image: str
) -> tuple[str, int]:
    """Extracts the question description from the given question image."""
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
    question_description: str, max_completion_tokens: int = MAX_COMPLETION_TOKENS
) -> tuple[str, int]:
    """Resolves the given question with an OpenAI pipeline using gpt-4o to describe the question and o1-preview to solve it."""

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


def resolve_exam(exam_path: str, questions_to_solve: list[int] = None) -> None:
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

    questions_images = questions_images + questions_images

    for i, question_image in tqdm(
        enumerate(questions_images, start=1),
        total=len(questions_images),
        desc="Processing Questions",
        unit="question",
    ):
        # Generate description
        tqdm.write(f"[Question {i}]\n├─ Generating description...")
        question_description, total_tokens = "teste", 100
        question_description, total_tokens = extract_question_description(
            question_image, conventions_image
        )
        tqdm.write(f"├─ Description generated ({total_tokens} tokens)")

        # Solve question
        tqdm.write(f"└─ Solving question...")
        answer, total_tokens = resolve_question(question_description)
        tqdm.write(f"└─ Solution found ({total_tokens} tokens)\n")

        # Save responses to file
        save_answer_and_description(answer, question_description, exam_path, i)


if __name__ == "__main__":
    resolve_exam("exams/ita_2025/math/essays", questions_to_solve=[1])
