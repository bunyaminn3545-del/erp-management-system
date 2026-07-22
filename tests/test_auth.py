import unittest

from app import app


class AuthTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page(self):
        response = self.app.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get("/register")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()