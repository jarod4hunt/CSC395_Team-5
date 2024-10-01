import unittest
import requests
from requests.auth import HTTPBasicAuth

class TestIntegration(unittest.TestCase):
    def test_integration_with_flask_server(self):
        url = 'http://localhost:5002/submit'
        payload = {
            'brand': 'TestBrand',
            'ingredients': 'flour, sugar, eggs'
	}
        response = requests.post(url, data=payload, auth=HTTPBasicAuth('csc395', 'team5'))
        self.assertEqual(response.status_code, 200)


        self.assertIn("Here is a recipe in the format you requested:", response.text)
        self.assertIn("TestBrand**", response.text)


if __name__ == '__main__':
    unittest.main()
