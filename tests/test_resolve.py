import pytest
import base64
import unittest.mock as mock
from gpt_resolve.resolve import (
    encode_image,
    resolve_question,
    process_questions,
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


def test_resolve_question_success():
    # Arrange
    question_image = "base64_encoded_image"
    conventions_image = "base64_encoded_conventions"
    expected_answer = "\section*{Solução}\nResposta teste\nANSWER: 42"
    expected_tokens = 100

    # Mock the OpenAI client's responses.create method
    mock_response = mock.Mock()
    mock_response.output_text = expected_answer
    mock_response.usage.total_tokens = expected_tokens

    mock_client = mock.Mock()
    mock_client.responses.create.return_value = mock_response

    # Act
    answer, tokens = resolve_question(
        question_image=question_image,
        conventions_image=conventions_image,
        client=mock_client,
        dry_run=False
    )

    # Assert
    assert answer == expected_answer
    assert tokens == expected_tokens
    mock_client.responses.create.assert_called_once()


def test_resolve_question_dry_run():
    # Test that dry_run returns expected mock response
    answer, tokens = resolve_question(
        question_image="dummy",
        conventions_image="dummy",
        dry_run=True
    )

    assert "Mock solution for testing purposes" in answer
    assert tokens == 200


def test_process_questions(tmp_path, monkeypatch):
    # Mock data
    question_images = [(1, "encoded_q1"), (2, "encoded_q2")]
    conventions_image = "encoded_conventions"
    exam_path = str(tmp_path)

    # Mock resolve_question to avoid actual API calls
    mock_answer = "\section*{Solução}\nTest answer\nANSWER: 42"
    mock_tokens = 100

    # Create a mock for save_answer_and_description
    with mock.patch('gpt_resolve.resolve.save_answer_and_description') as mock_save:
        with mock.patch('gpt_resolve.resolve.resolve_question',
                      return_value=(mock_answer, mock_tokens)) as mock_resolve:

            # Call the function
            process_questions(
                questions_images=question_images,
                conventions_image=conventions_image,
                exam_path=exam_path,
                dry_run=True,
                max_tokens_output=1000,
                model="test-model"
            )

            # Verify the mocks were called correctly
            assert mock_resolve.call_count == 2
            assert mock_save.call_count == 2

            # Check the arguments for the first question
            mock_resolve.assert_any_call(
                question_image="encoded_q1",
                conventions_image="encoded_conventions",
                model="test-model",
                dry_run=True,
                max_tokens_output=1000,
                client=None
            )

            # Check save was called with correct arguments
            mock_save.assert_any_call(
                mock_answer,
                mock.ANY,  # question_description
                exam_path,
                1,
                "test-model",
                dry_run=True
            )
