from dotenv import load_dotenv
import os
import glob
import base64

from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)
MAX_TOKENS_QUESTION_DESCRIPTION = 400
MAX_TOKENS_ANSWER = 5000


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_exam_images_paths(path: str):
    """
    Returns the paths of the images of the exam.
    The 'convencoes.jpg' file is the conventions of the exam and will be included in every question.
    """
    conventions_path = glob.glob(path + "/conventions.jpg")[0]
    questions_paths = [
        p for p in glob.glob(path + "/*.jpg") if "conventions" not in p.lower()
    ]

    return conventions_path, questions_paths


def extract_question_description(question_image: str, conventions_image: str):
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
                            "Use a notação LaTeX para toda a sua resposta."
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
    question_description: str, max_tokens_answer: int = MAX_TOKENS_ANSWER
):
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
                            "Use a notação LaTeX para toda a sua resposta, inclusive para separar as partes da solução ou destacar palavras e títulos."
                            "Indique a solução final com um 'ANSWER:' seguido do resultado."
                            f"O enunciado da questão é:\n\n```{question_description}```"
                        ),
                    },
                ],
            }
        ],
        max_completion_tokens=max_tokens_answer,
    )
    answer = response.choices[0].message.content
    total_tokens = response.usage.total_tokens

    return answer, total_tokens


def resolve_exam(exam_path: str):
    """Resolves the given exam with GPT."""

    conventions_path, questions_paths = get_exam_images_paths(exam_path)

    # Encode the images
    conventions_image = encode_image(conventions_path)
    questions_images = [encode_image(p) for p in questions_paths]

    # Store all responses and question descriptions in text
    answers = []
    question_descriptions = []

    # Process each question
    for i, question_image in enumerate(questions_images, 1):
        print(f"Generating description for question {i}...", end="")
        question_description, total_tokens = extract_question_description(
            question_image, conventions_image
        )
        print(f"Total tokens: {total_tokens}")
        question_descriptions.append(question_description)

        # Additionally, generate a text version of the question to use with o1-preview
        print(f"\tSolving question {i}...", end="")
        answer, total_tokens = resolve_question(question_description)
        print(f"Total tokens: {total_tokens}")
        answers.append(answer)

    # Save responses to file
    with open(f"{exam_path}/solutions.txt", "w", encoding="utf-8") as f:
        for i, answer in enumerate(answers, 1):
            f.write(f"\\section*{{Questão {i}}}\n")
            f.write("=" * 50 + "\n")
            f.write(answer + "\n\n")

    with open(f"{exam_path}/descriptions.txt", "w", encoding="utf-8") as f:
        for i, description in enumerate(question_descriptions, 1):
            f.write(f"\\section*{{Questão {i}}}\n")
            f.write("=" * 50 + "\n")
            f.write(description + "\n\n")


if __name__ == "__main__":
    resolve_exam("exams/ita_2025/math/essays")
