from application import app
from flask import jsonify
from random import choice

# Declaring the card deck values
values = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

# Route to get a random card deck suit
@app.route('/get-values', methods=['GET'])
def get_values():
    value = choice(values)
    return jsonify(value=value)