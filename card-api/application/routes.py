from application import app
from flask import request, jsonify, Response

@app.route('/get-card', methods=['POST'])
def card():
    card_data = request.get_json()
    card_value = card_data["Value"]
    card_suit = card_data["Suit"]
    values = {"Ace":"Ace", "Two":"Two", "Three":"Three", "Four":"Four", "Five":"Five", "Six":"Six", "Seven":"Seven", "Eight":"Eight", "Nine":"Nine", "Ten":"Ten", "Jack":"Jack", "Queen":"Queen", "King":"King"}
    suits = {"Clubs":"Clubs", "Diamonds":"Diamonds", "Hearts":"Hearts", "Spades":"Spades"}
    selected_card = f"{values[card_value]} of {suits[card_suit]}"
    return Response(selected_card, mimetype='text/plain')