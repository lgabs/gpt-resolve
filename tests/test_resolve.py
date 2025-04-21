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


@pytest.mark.asyncio
async def test_process_questions(tmp_path, monkeypatch):
    # Mock data
    question_images = [(1, "encoded_q1"), (2, "encoded_q2")]
    conventions_image = "encoded_conventions"
    exam_path = str(tmp_path)

    # Create fake futures that will be returned by our mock process_question
    future1 = asyncio.Future()
    future1.set_result((1, 100))  # (question_num, tokens)

    future2 = asyncio.Future()
    future2.set_result((2, 100))

    # Mock process_question
    with mock.patch('gpt_resolve.resolve.process_question') as mock_process:
        # Set up the mock to return prepared futures
        mock_process.side_effect = [future1, future2]

        # Mock asyncio.as_completed to return our futures in a controlled order
        with mock.patch('asyncio.as_completed', return_value=[future1, future2]):
            # Run the actual function
            await process_questions(
                questions_images=question_images,
                conventions_image=conventions_image,
                exam_path=exam_path,
                dry_run=True,
                max_tokens_output=1000,
                model="test-model"
            )

            # Verify process_question was called for each question
            assert mock_process.call_count == 2
