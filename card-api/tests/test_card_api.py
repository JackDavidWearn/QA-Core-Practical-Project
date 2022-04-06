from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app

# Creating the TestBase, which returns the created application
class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_get_ace_clubs(self):
        response = self.client.post(url_for('card'), json={"symbol": "A", "suit": "Clubs"})
        self.assert200(response)
        self.assertIn(b'static/clubs_A.png', response.data)


    