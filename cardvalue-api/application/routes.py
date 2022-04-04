from application import app
from flask import Response
from random import choice

# Declaring the card deck values
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Route to get a random card deck suit
@app.route('/get-values', methods=['GET'])
def get_values():
    value = choice(values)
    return Response(value, mimetype="text/plain")