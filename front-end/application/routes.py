from application import app
from flask import render_template
from application.models import Cards
import requests

@app.route('/')
def index():
    symbol = requests.get('http://cardvalue-api:5000/get_value')
    suit = requests.get('http://cardsuit-api:5000/get_suit')
    card = {"symbol":symbol.text, "suit":suit.text}
    card_gen = requests.post('http://card-api:5000/card', json=card)
    json = card_gen.json()
    value = json["value"]
    return render_template('index.html', value=value, suit=suit.text)