import unittest
import json
from app import create_app

class AppTestCase(unittest.TestCase):
    """This class represents the app test case"""
    def setUp(self):
            """Define test variables and initialize app."""
            self.app = create_app()
            self.client = self.app.test_client

    def test_400_non_number_input(self):
        res = self.client().post(
            '/api/two-numbers',
            json={'num1': 100, "num2" :"somesting"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_400_only_one_number_provided(self):
        res = self.client().post(
            '/api/two-numbers',
            json={'num1': 100})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
    
    def test_400_number_not_within_range(self):
        res = self.client().post(
            '/api/two-numbers',
            json={'num1': 100, "num2" :10**15})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)


    def test_zero_division(self):
        res = self.client().post(
            '/api/two-numbers',
            json={'num1': 100, "num2" :0})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['results']['division'], "Error, Zero division")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()