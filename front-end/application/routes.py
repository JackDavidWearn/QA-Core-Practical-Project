from application import app, db
from application.models import Cards
from flask import render_template
import requests
from datetime import date

@app.route('/')
def index():
    symbol = requests.get('http://cardvalue-api:5000/get-values')
    suit = requests.get('http://cardsuit-api:5000/get-suit')
    card = {"symbol": symbol.text, "suit": suit.text}
    card_gen = requests.post('http://card-api:5000/card', json=card)
    json = card_gen.json()
    image = json["image"]
    value = json["value"]
    image_save = f'{json["image"]}'
    add = Cards(cards_value=symbol.text, cards_suit=suit.text, date_generated=date.today())
    db.session.add(add)
    db.session.commit()
    results = Cards.query.order_by(Cards.id.desc()).limit(5).all()
    return render_template('index.html', symbol=symbol.text, suit=suit.text, image=image_save, value=value, results=results)

@app.route('/history', methods=['GET'])
def history():
    events_history = Cards.query.all()
    return render_template('history.html', events_history = events_history)