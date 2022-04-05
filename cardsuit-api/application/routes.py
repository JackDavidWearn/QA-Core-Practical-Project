from application import app
from flask import Response
from random import choice

# Route to get a random card deck suit
@app.route('/get-suit', methods=['GET'])
def get_suit():
    # Declaring the 4 card deck suits
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    suit = choice(suits)
    return Response(suit, mimetype="text/plain")