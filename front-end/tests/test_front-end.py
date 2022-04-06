from application import app, db
from application.models import Cards
from flask import url_for
import requests_mock
from flask_testing import TestCase
from datetime import date

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
    
    def setUp(self):
        sample_result = Cards(card_value='K', card_suit='Clubs', date_generated=date(2022, 4, 5))
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend_home(self):
        suit = "Diamonds"
        symbol = "King"
        value = "King of Diamonds"
        image = "static/diamonds_K.png"

        with requests_mock.Mocker() as m:
            m.get('http://cardvalue-api:5000/get-values', text=symbol)
            m.get('http://cardsuit-api:5000/get_suit', text=suit)
            m.post('http://card-api:5000/card', json={"value":value, "suit":suit, "image":image})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'King of Clubs', response.data)
            self.assertIn(b'King of Diamonds', response.data)
            self.assertIn(b'static/diamonds_k.png', response.data)

def test_get_history(self):
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'K of Clubs', response.data)