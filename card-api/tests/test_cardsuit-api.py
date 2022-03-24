from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

# Creating the TestBase, which returns the created application
class TestBase(TestCase):
    def create_app(self):
        return app

# TestView, inherits from TestBase, and used to test all choice operations
class TestView(TestBase):
    # Testing for Clubs in random choice
    @patch('application.routes.choice', return_value='Clubs')
    def test_get_suit_clubs(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertIn(b'Clubs', response.data)

    # Testing for Diamonds in random choice
    @patch('application.routes.choice', return_value='Diamonds')
    def test_get_suit_diamonds(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertIn(b'Diamonds', response.data)

    # Testing for Hearts in random choice
    @patch('application.routes.choice', return_value='Hearts')
    def test_get_suit_hearts(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertIn(b'Hearts', response.data)

    # Testing for Spades in random choice
    @patch('application.routes.choice', return_value='Spades')
    def test_get_suit_spades(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertIn(b'Spades', response.data)

    # Testing for non-existant choice in random choice
    @patch('application.routes.choice', return_value='Joker')
    def test_get_suit_not_exists(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertNotIn(b'Joker', response.data)