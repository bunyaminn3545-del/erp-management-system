import unittest

from app import app


class OrderTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_order_page(self):
        response = self.app.get("/orders")
        self.assertIn(response.status_code, [200, 302])


if __name__ == "__main__":
    unittest.main()