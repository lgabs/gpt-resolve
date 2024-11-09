import glob
import os


def get_exam_images_paths(path: str) -> tuple[str, list[tuple[int, str]]]:
    """
    Returns the paths of the images of the exam.
    The 'conventions.jpg' file is the conventions of the exam and will be included in every question.
    Returns:
        tuple: (conventions_path, [(question_number, question_path), ...])
        The questions list is sorted by question number.
    """
    conventions_path = glob.glob(path + "/conventions.jpg")[0]

    # Get all jpg files except conventions
    question_files = [
        p for p in glob.glob(path + "/*.jpg") if "conventions" not in p.lower()
    ]

    # Extract question numbers and create tuples of (number, path)
    questions_with_numbers = []
    for path in question_files:
        filename = os.path.basename(path)
        if filename.startswith("q"):
            try:
                question_number = int(filename[1:].split(".")[0])
                questions_with_numbers.append((question_number, path))
            except ValueError as e:
                raise ValueError(
                    f"Error extracting question number from {filename}: {e}. Questions should be named like 'q1.jpg', 'q2.jpg', etc."
                )

    questions_with_numbers.sort(key=lambda x: x[0])

    return conventions_path, questions_with_numbers


def save_answer_and_description(
    answer: str,
    question_description: str,
    exam_path: str,
    question_number: int,
    dry_run: bool = False,
) -> None:
    """Saves the answer and question description to files."""

    solutions_path = (
        f"{exam_path}/solutions" if not dry_run else f"{exam_path}/solutions_dry_run"
    )
    os.makedirs(solutions_path, exist_ok=True)

    with open(
        f"{solutions_path}/q{question_number}_solution.txt", "w", encoding="utf-8"
    ) as f:
        f.write(question_description + "\n\n")
        f.write(answer)
