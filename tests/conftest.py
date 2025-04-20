import pytest
from unittest.mock import Mock, patch


@pytest.fixture
def temp_exam_dir(tmp_path):
    """Create a temporary exam directory with test files."""
    # Create test files
    conventions = tmp_path / "conventions.jpg"
    q1 = tmp_path / "q1.jpg"
    q2 = tmp_path / "q2.jpg"
    q3 = tmp_path / "q3.jpg"

    # Create empty files
    for f in [conventions, q1, q2, q3]:
        f.touch()

    return tmp_path


@pytest.fixture
def temp_exam_dir_invalid(tmp_path):
    """Create a temporary exam directory with invalid test files."""
    # Create test files with invalid naming
    conventions = tmp_path / "conventions.jpg"
    valid_q = tmp_path / "q1.jpg"
    invalid_q = tmp_path / "qinvalid.jpg"  # Invalid question format
    another_invalid = tmp_path / "question2.jpg"  # Doesn't follow q{number} format

    # Create empty files
    for f in [conventions, valid_q, invalid_q, another_invalid]:
        f.touch()

    return tmp_path
