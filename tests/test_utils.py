import pytest
import os
from gpt_resolve.utils import get_exam_images_paths


def test_get_exam_images_paths_basic(temp_exam_dir):
    """Test basic functionality with properly named files."""
    conventions_path, questions = get_exam_images_paths(str(temp_exam_dir))

    assert os.path.basename(conventions_path) == "conventions.jpg"
    assert len(questions) == 3
    assert [(num, os.path.basename(path)) for num, path in questions] == [
        (1, "q1.jpg"),
        (2, "q2.jpg"),
        (3, "q3.jpg"),
    ]


def test_get_exam_images_invalid_files(temp_exam_dir_invalid):
    """Test handling of invalid file names in exam directory."""
    with pytest.raises(ValueError) as exc_info:
        get_exam_images_paths(str(temp_exam_dir_invalid))
