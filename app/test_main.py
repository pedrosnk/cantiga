from fastapi.testclient import TestClient
from unittest import TestCase

from .main import app

client = TestClient(app)


class AppTest(TestCase):
    def test_request_home_page(self):
        response = client.get('/')
        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertRegex(
            response.text,
            'Cantiga',
        )
