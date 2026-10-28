import pytest


@pytest.fixture
def temp_exam_dir(tmp_path):
    """Create a temporary exam directory with test files."""
    for name in ["conventions.jpg", "q1.jpg", "q2.jpg", "q3.jpg"]:
        (tmp_path / name).touch()
    return tmp_path


@pytest.fixture
def temp_exam_dir_invalid(tmp_path):
    """Create a temporary exam directory with invalid test files."""
    # qinvalid.jpg is invalid; question2.jpg doesn't follow q{number} and is ignored
    for name in ["conventions.jpg", "q1.jpg", "qinvalid.jpg", "question2.jpg"]:
        (tmp_path / name).touch()
    return tmp_path
