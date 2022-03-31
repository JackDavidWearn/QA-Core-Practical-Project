from application import app
from flask import Flask, request, Response, jsonify

@app.route('/get-card', methods=['POST'])
def card():
    cards = request.get_json()
    symbol = cards["value"]
    suit = cards["suit"]
    values = {'A':'Ace', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King'}
    value = values[symbol]
    return jsonify({"value":value, "suit":suit})
    