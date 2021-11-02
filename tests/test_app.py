import unittest
import requests

class AppTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:5000'

    def test_hallo(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.json()

        self.assertEqual(content['hello'], "world")
        self.assertEqual(status_code, 200)

    def test_addition(self):
        response = requests.post(self.url + "/add", json={"zahleins":3,"zahlzwei":4})
        status_code = response.status_code
        content = response.json()
        self.assertEqual(content['ergebnis'], 7)
        self.assertEqual(status_code, 200)

    def test_status(self):
        response = requests.get(self.url + "/status")
        status_code = response.status_code
        content = response.json()
        print(str(content['my_ip']))
        self.assertEqual(content['state'], "alive")
        self.assertEqual(status_code, 200)

if __name__ == "__main__":
    unittest.main()
