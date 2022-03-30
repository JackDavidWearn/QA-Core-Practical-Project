from application import app
from flask import Flask, request, Response
import random


# Declaring the 4 card deck suits
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Route to get a random card deck suit
@app.route('/get-suit', methods=['GET'])
def get_suit():
    # suit = choice(suits)
    # return Response(suit)
    suits = random.choice(['Clubs', 'Diamonds', 'Hearts', 'Spades'])
    return Response(suits, mimetype='text/plain')