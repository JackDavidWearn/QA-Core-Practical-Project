from application import app
from flask import request, jsonify

@app.route('/card', methods=['POST'])
def card():
    card_json = request.get_json()
    card_value = card_json["value"]
    card_suit = card_json["suit"]
    string = f'{card_value} of {card_suit}'
    return string