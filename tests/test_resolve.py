import pytest
import base64
from gpt_resolve.resolve import (
    encode_image,
    extract_question_description,
    resolve_question,
)


def test_encode_image_success(tmp_path):
    # Create a temporary test image
    test_image = tmp_path / "test_image.jpg"
    test_content = b"test image content"
    test_image.write_bytes(test_content)

    # Test encoding
    result = encode_image(str(test_image))

    # Verify the result is a valid base64 string
    assert isinstance(result, str)
    # Verify we can decode it back to the original content
    assert base64.b64decode(result) == test_content


def test_encode_image_file_not_found():
    # Test with non-existent file
    with pytest.raises(FileNotFoundError):
        encode_image("nonexistent_image.jpg")


def test_encode_image_invalid_path():
    # Test with invalid path
    with pytest.raises(OSError):
        encode_image("")


def test_extract_question_description_success(mock_question_description_client):
    # Arrange
    question_image = "base64_encoded_image"
    conventions_image = "base64_encoded_conventions"
    expected_description = "\section*{Questão 1}\n\nEnunciado teste"
    expected_tokens = 100

    # Act
    description, tokens = extract_question_description(
        mock_question_description_client, question_image, conventions_image
    )

    # Assert
    assert description == expected_description
    assert tokens == expected_tokens
    mock_question_description_client.chat.completions.create.assert_called_once()


def test_resolve_question_success(mock_answer_client):
    # Arrange
    question_description = "\section*{Questão 1}\n\nEnunciado teste"
    expected_answer = "\section*{Solução}\nResposta teste\nANSWER: 42"
    expected_tokens = 100

    # Act
    answer, tokens = resolve_question(mock_answer_client, question_description)

    # Assert
    assert answer == expected_answer
    assert tokens == expected_tokens
    mock_answer_client.chat.completions.create.assert_called_once()
