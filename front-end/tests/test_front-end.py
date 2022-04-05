from application import app, db
from application.models import Cards
from flask import url_for
import requests_mock
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
    
    def setUp(self):
        sample_result = Cards(card_value='K', card_suit='Clubs')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://cardvalue-api:5000/get-values', Response="Q")
            m.get('http://cardsuit-api:5000/get_suit', Response="Diamonds")
            m.post('http://card-api:5000/card', json={"symbol":"Q", "suit":"Diamonds"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'King of Clubs', response.data)
            self.assertIn(b'Queen of Diamonds', response.data)