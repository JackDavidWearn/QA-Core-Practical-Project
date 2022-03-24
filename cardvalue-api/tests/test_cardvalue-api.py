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
    # Testing for Ace in random choice
    @patch('application.routes.choice', return_value='Ace')
    def test_get_values_ace(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Ace', response.data)
    
    # Testing for Two in random choice
    @patch('application.routes.choice', return_value='Two')
    def test_get_values_two(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Two', response.data)

    # Testing for Three in random choice
    @patch('application.routes.choice', return_value='Three')
    def test_get_values_three(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Three', response.data)

    # Testing for Four in random choice
    @patch('application.routes.choice', return_value='Four')
    def test_get_values_four(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Four', response.data)

    # Testing for Five in random choice
    @patch('application.routes.choice', return_value='Five')
    def test_get_values_five(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Five', response.data)

    # Testing for Six in random choice
    @patch('application.routes.choice', return_value='Six')
    def test_get_values_six(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Six', response.data)

    # Testing for Seven in random choice
    @patch('application.routes.choice', return_value='Seven')
    def test_get_values_seven(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Seven', response.data)

    # Testing for Eight in random choice
    @patch('application.routes.choice', return_value='Eight')
    def test_get_values_eight(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Eight', response.data)

    # Testing for Nine in random choice
    @patch('application.routes.choice', return_value='Nine')
    def test_get_values_nine(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Nine', response.data)

    # Testing for Ten in random choice
    @patch('application.routes.choice', return_value='Ten')
    def test_get_values_ten(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Ten', response.data)

    # Testing for Jack in random choice
    @patch('application.routes.choice', return_value='Jack')
    def test_get_values_jack(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Jack', response.data)

    # Testing for Queen in random choice
    @patch('application.routes.choice', return_value='Queen')
    def test_get_values_queen(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'Queen', response.data)

    # Testing for King in random choice
    @patch('application.routes.choice', return_value='King')
    def test_get_values_king(self, mock_func):
        response = self.client.get(url_for('get_values'))
        self.assert200(response)
        self.assertIn(b'King', response.data)

    # Testing for non-existant choice in random choice
    @patch('application.routes.choice', return_value='Joker')
    def test_get_values_not_exists(self, mock_func):
        response = self.client.get(url_for('get_suit'))
        self.assert200(response)
        self.assertNotIn(b'Joker', response.data)