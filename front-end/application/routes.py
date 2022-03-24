from application import app
from flask import render_template
from application.models import Cards
import requests

@app.route('/')
def index():
    card_value = requests.get('http://cardvalue-api:5000/get_value')
    card_suit = requests.get('http://cardsuit-api:5000/get_suit')
    selected_card = requests.post('http://card_api:5000/get_card', json = {"Value": card_value.text, "Suit": card_suit.text})
    cards = Cards(card_value = card_value.text, card_suit = card_suit.text)
    db.session.add(cards)
    db.session.commit()
    return render_template('index.html', cards = cards)