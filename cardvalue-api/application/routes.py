from application import app
from flask import Flask, request, Response
import random

# Declaring the card deck values
# symbols = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Route to get a random card deck suit
@app.route('/get-values', methods=['GET'])
def get_values():
    # symbol = choice(symbols)
    # return Response(symbol)
    symbols = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    return Response(symbols, mimetype='text/plain')