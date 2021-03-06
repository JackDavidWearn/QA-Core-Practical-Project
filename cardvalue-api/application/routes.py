from application import app
from flask import Response
from random import choice

# Route to get a random card deck suit
@app.route('/get-values', methods=['GET'])
def get_values():
    # Declaring the card deck values
    symbols = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    symbol = choice(symbols)
    return Response(symbol, mimetype="text/plain")