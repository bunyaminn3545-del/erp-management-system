import unittest

from app import app


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_customer_page(self):
        response = self.app.get("/customers")
        self.assertIn(response.status_code, [200, 302])


if __name__ == "__main__":
    unittest.main()