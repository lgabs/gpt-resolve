import pytest
import base64
import unittest.mock as mock
import asyncio
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
    """Test that process_questions passes the correct parameters to asyncio.run()"""
    # Create needed files in the temporary directory
    conventions_file = tmp_path / "conventions.jpg"
    q1_file = tmp_path / "q1.jpg"
    q2_file = tmp_path / "q2.jpg"

    # Create empty files
    conventions_file.write_bytes(b"test content")
    q1_file.write_bytes(b"test content")
    q2_file.write_bytes(b"test content")

    exam_path = str(tmp_path)

    # Mock necessary functions to avoid real file operations or API calls
    with mock.patch('gpt_resolve.resolve.encode_image', return_value="mock_encoded_image"):
        with mock.patch('asyncio.run') as mock_async_run:
            # Import the function that uses process_questions
            from gpt_resolve.resolve import resolve_exam

            # Call the function that would use process_questions
            resolve_exam(
                exam_path=exam_path,
                questions_to_solve=[1, 2],
                dry_run=True,
                max_tokens_output=1000,
                model="test-model"
            )

            # Verify asyncio.run was called
            assert mock_async_run.call_count == 1

            # Get the arguments passed to asyncio.run
            args, _ = mock_async_run.call_args

            # Check that the first argument is a coroutine object (process_questions)
            assert callable(args[0].__await__)
