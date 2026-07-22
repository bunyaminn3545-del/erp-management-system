import unittest

from app import app


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_product_page(self):
        response = self.app.get("/products")
        self.assertIn(response.status_code, [200, 302])


if __name__ == "__main__":
    unittest.main()