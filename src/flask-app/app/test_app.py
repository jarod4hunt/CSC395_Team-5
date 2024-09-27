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
    
		with patch('requests.post', return_value=mock_response):
			result = list(stream_ollama_response(prompt))
    
		assert result == ["Recipe Title:", "Fun Tagline"]



if __name__== '__main__':
	unittest.main()

