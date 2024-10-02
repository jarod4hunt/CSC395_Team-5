import unittest
from unittest.mock import patch, MagicMock
import requests
from app import stream_ollama_response


class BasicTest(unittest.TestCase):

	def test_always_passes(self):
		self.assertTrue(True)


	def test_stream_ollama_response_success(self):
		prompt = "Make a cake"
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.iter_lines.return_value = [
			b'{"response": "Recipe Title:", "done": false}',
			b'{"response": "Fun Tagline", "done": true}'
		]
		mock_response.text = "OK"		

		# Configure the mock to behave like a context manager
		mock_post = MagicMock()
		mock_post.__enter__.return_value = mock_response
		mock_post.__exit__.return_value = None  # Just to make sure it behaves correctly

    
		with patch('requests.post', return_value=mock_post):
			result = list(stream_ollama_response(prompt))
    
		assert result == ["Recipe Title:", "Fun Tagline"]




	def test_stream_ollama_response_failure(self):
		prompt = "Make a cake"
		mock_response = MagicMock()
		mock_response.status_code = 500
		mock_response.text = "Internal Server Error"

		mock_post = MagicMock()
		mock_post.__enter__.return_value = mock_response
		mock_post.__exit__.return_value = None
		
		with patch('requests.post', return_value=mock_post):
			result = list(stream_ollama_response(prompt))

		self.assertEqual(result, ["Error communicating with Ollama: 500 Internal Server Error"])

	def test_stream_ollama_response_invalid_json(self):
		prompt = "Make a cake"
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.iter_lines.return_value = [
			b'{"response": "Recipe Title:"',
			b'invalid_json_line'
		]
		mock_response.text = "OK"
		
		mock_post = MagicMock()
		mock_post.__enter__.return_value = mock_response
		mock_post.__exit__.return_value = None

		with patch('requests.post', return_value=mock_post):
			result = list(stream_ollama_response(prompt))
		self.assertEqual(result, [
			"Error parsing JSON: b'{\"response\": \"Recipe Title:\"'",
			"Error parsing JSON: b'invalid_json_line'"
		])

	def test_stream_ollama_response_timeout(self):


		prompt = "Make a cake"


		mock_post = MagicMock()
		mock_post.side_effect = requests.exceptions.Timeout

		with patch('requests.post', mock_post):
			result = list(stream_ollama_response(prompt))

		self.assertEqual(result, ["Request failed: "])

	def test_stream_ollama_response_invalid_status_code(self):

		prompt = "Make a cake"

		mock_response = MagicMock()
		mock_response.status_code = 403

		mock_response.text = "Forbidden"

		mock_post = MagicMock()

		mock_post.__enter__.return_value = mock_response

		mock_post.__exit__.return_value = None

		with patch('requests.post', return_value=mock_post):

			result = list(stream_ollama_response(prompt))

		self.assertEqual(result, ["Error communicating with Ollama: 403 Forbidden"])

if __name__== '__main__':
	unittest.main()

