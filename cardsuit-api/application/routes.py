from application import app
from flask import Flask, request, Response
from random import choice


# Declaring the 4 card deck suits
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Route to get a random card deck suit
@app.route('/get-suit', methods=['GET'])
def get_suit():
    suit = choice(suits)
    return Response(suit)