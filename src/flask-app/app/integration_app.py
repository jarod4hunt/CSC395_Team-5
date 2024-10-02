import unittest
import requests
from requests.auth import HTTPBasicAuth

class TestIntegration(unittest.TestCase):
    def test_integration_with_flask_server(self):
        url = 'http://localhost:5000/submit'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'ingredients': 'tomatoes, cheese, pasta',
            'brand': 'Kraft'
	}
        auth = HTTPBasicAuth('csc395', 'team5')
        response = requests.post(url, headers=headers, data=payload, auth=auth)
        self.assertEqual(response.status_code, 200)


        self.assertIn('Kraft', response.text, "Kraft not found in the reply!")


if __name__ == '__main__':
    unittest.main()
