from application import app
# from application.models import Cards
from flask import render_template
import requests

@app.route('/')
def index():
    value = requests.get('http://cardvalue-api:5000/get-values')
    suit = requests.get('http://cardsuit-api:5000/get-suit')
    card = {"value": value.text, "suit": suit.text}
    card_gen = requests.post('http://card-api:5000/card', json=card)
    json = card_gen.json()
    image = json["image"]
    card_value = json["value"]
    return render_template('index.html', image=image, card_value=card_value, suit=suit.text)




    # value = requests.get('http://cardvalue-api:5000/get-values')
    # suit = requests.get('http://cardsuit-api:5000/get-suit')
    # card = requests.post('http://card-api:5000/card', json=dict(value=value.json()["value"], suit=suit.json()["suit"]))
    # db.session.add(Cards(cards_value=value.json()["value"], cards_suit=suit.json()["suit"]))
    # db.session.commit()
    # results = Cards.query.all()
    # return render_template('index.html', results = results)