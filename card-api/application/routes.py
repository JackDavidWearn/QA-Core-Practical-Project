from application import app
from flask import request, jsonify

card_deck = {'SpadesA':'static/spades_A.png', 'Spades2':'static/spades_2.png', 'Spades3':'static/spades_3.png','Spades4':'static/spades_4.png','Spades5':'static/spades_5.png','Spades6':'static/spades_6.png', 'Spades7':'static/spades_7.png','Spades8':'static/spades_8.png','Spades9':'static/spades_9.png','Spades10':'static/spades_10.png','SpadesJ':'static/spades_J.png','SpadesQ':'static/spades_Q.png','SpadesK':'static/spades_K.png', 'DiamondsA':'static/diamonds_A.png', 'Diamonds2':'static/diamonds_2.png', 'Diamonds':'static/diamonds_3.png','Diamonds':'static/diamonds_4.png','Diamonds':'static/diamonds_5.png','Diamonds':'static/diamonds_6.png', 'Diamonds':'static/diamonds_7.png','Diamonds':'static/diamonds_8.png','Diamonds':'static/diamonds_9.png','Diamonds':'static/diamonds_10.png','Diamonds':'static/diamonds_J.png','Diamonds':'static/diamonds_Q.png','Diamonds':'static/diamonds_K.png','HeartsA':'static/hearts_A.png', 'Hearts2':'static/hearts_2.png', 'Hearts3':'static/hearts_3.png','Hearts4':'static/hearts_4.png','Hearts5':'static/hearts_5.png','Hearts6':'static/hearts_6.png', 'Hearts7':'static/hearts_7.png','hearts8':'static/hearts_8.png','Hearts9':'static/hearts_9.png','Hearts10':'static/hearts_10.png','HeartsJ':'static/hearts_J.png','HeartsQ':'static/hearts_q.png','HeartsK':'static/hearts_K.png','SpadesA':'static/spades_A.png', 'Spades2':'static/spades_2.png', 'Spades3':'static/spades_3.png','Spades4':'static/spades_4.png','Spades5':'static/spades_5.png','Spades6':'static/spades_6.png', 'Spades7':'static/spades_7.png','Spades8':'static/spades_8.png','Spades9':'static/spades_9.png','Spades10':'static/spades_10.png','SpadesJ':'static/spades_J.png','SpadesQ':'static/spades_Q.png','SpadesK':'static/spades_K.png',}

@app.route('/card', methods=['POST'])
def card():
    cards = request.get_json()
    symbol = cards["symbol"]
    suit = cards["suit"]
    card_image_key = suit+symbol
    print(card_image_key)
    card_image = card_deck[card_image_key]
    values = {'A':'Ace', 
              '2':'Two', 
              '3':'Three', 
              '4':'Four', 
              '5':'Five', 
              '6':'Six', 
              '7':'Seven', 
              '8':'Eight', 
              '9':'Nine', 
              '10':'Ten', 
              'J':'Jack', 
              'Q':'Queen', 
              'K':'King' 
            }
    value = values[symbol]
    return jsonify({"value": value, "suit": suit, "image": card_image})