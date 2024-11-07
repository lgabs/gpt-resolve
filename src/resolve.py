import glob
import base64

from openai import OpenAI


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


client = OpenAI()


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
                            "Caso haja imagens, descreva-as de forma clara e objetiva de forma que seja possível entender o problema."
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
        max_tokens=400,
    )
    return response.choices[0]


def resolve_question(question_description: str):
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Você é um especialista em matemática resolvendo questões de admissão universitária do ITA. "
                            "Responda à questão de forma clara e objetiva, explicando o raciocínio passo a passo, mas mantenha o foco na solução."
                            "Use a notação LaTeX para toda a sua resposta, inclusive para separar as partes da solução."
                            "Indique a solução final com um 'ANSWER:' seguido do resultado."
                            f"O enunciado da questão é:\n\n{question_description.message.content}"
                        ),
                    },
                ],
            }
        ],
        max_completion_tokens=5000,
    )

    return response.choices[0]


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
        print(f"Gerando a descrição da questão {i}...")
        question_description = extract_question_description(question_image, conventions_image)
        question_descriptions.append(question_description)

        # Additionally, generate a text version of the question to use with o1-preview
        print(f"\tResolvendo a questão {i}...")
        answer = resolve_question(question_description)

        answers.append(answer.message.content)

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
            f.write(description.message.content + "\n\n")


if __name__ == "__main__":
    resolve_exam("exams/ita_2025/math/essays")
