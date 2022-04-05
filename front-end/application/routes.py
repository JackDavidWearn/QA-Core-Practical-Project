from application import app
# from application.models import Cards
from flask import render_template
import requests
from PIL import Image

@app.route('/')
def index():
    symbol = requests.get('http://cardvalue-api:5000/get-values')
    suit = requests.get('http://cardsuit-api:5000/get-suit')
    card = {"symbol": symbol.text, "suit": suit.text}
    card_gen = requests.post('http://card-api:5000/card', json=card)
    json = card_gen.json()
    image = json["image"]
    value = json["value"]
    image_save = Image.open('{image}')
    # image_save = f'{json["image"]}'
    return render_template('index.html', symbol=symbol.text, suit=suit.text, image=image_save, value=value)




    # value = requests.get('http://cardvalue-api:5000/get-values')
    # suit = requests.get('http://cardsuit-api:5000/get-suit')
    # card = requests.post('http://card-api:5000/card', json=dict(value=value.json()["value"], suit=suit.json()["suit"]))
    # db.session.add(Cards(cards_value=value.json()["value"], cards_suit=suit.json()["suit"]))
    # db.session.commit()
    # results = Cards.query.all()
    # return render_template('index.html', results = results)