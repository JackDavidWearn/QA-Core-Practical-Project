from application import app, db
from application.models import Cards
from flask import render_template
import requests

@app.route('/')
def index():
    value = requests.get('http://cardvalue-api:5000/get-values')
    suit = requests.get('http://cardsuit-api:5000/get-suit')
    card = requests.post('http://card-api:5000/card', json=dict(value=value.json()["value"], suit=suit.json()["suit"]))
    db.session.add(Cards(cards_value=value.json()["value"], cards_suit=suit.json()["suit"]))
    db.session.commit()
    results = Cards.query.all()
    return render_template('index.html', results = results)