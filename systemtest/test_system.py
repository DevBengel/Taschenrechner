import unittest
import requests
import json
import re

class AppTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:3333'

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


    def test_lb(self):
        response1 = requests.get(self.url + '/status')
        response2 = requests.get(self.url + '/status')
         
        content1 = response1.json()
        content2 = response2.json()

        my_ip1 = str(content1['my_ip'])
        my_ip2 = str(content2['my_ip'])
        
        self.assertIsNot(my_ip1, None)
        self.assertIsNot(my_ip2, None)
        self.assertNotEqual(my_ip1, my_ip2)

if __name__ == "__main__":
    unittest.main()
