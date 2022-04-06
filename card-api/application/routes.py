from application import app
from flask import request, jsonify

card_deck = {'SpadesA':'spades_A.png',
             'Spades2':'spades_2.png', 
             'Spades3':'spades_3.png',
             'Spades4':'spades_4.png',
             'Spades5':'spades_5.png',
             'Spades6':'spades_6.png', 
             'Spades7':'spades_7.png',
             'Spades8':'spades_8.png',
             'Spades9':'spades_9.png',
             'Spades10':'spades_10.png',
             'SpadesJ':'spades_J.png',
             'SpadesQ':'spades_Q.png',
             'SpadesK':'spades_K.png', 
             'DiamondsA':'diamonds_A.png', 
             'Diamonds2':'diamonds_2.png', 
             'Diamonds3':'diamonds_3.png',
             'Diamonds4':'diamonds_4.png',
             'Diamonds5':'diamonds_5.png',
             'Diamonds6':'diamonds_6.png', 
             'Diamonds7':'diamonds_7.png',
             'Diamonds8':'diamonds_8.png',
             'Diamonds9':'diamonds_9.png',
             'Diamonds10':'diamonds_10.png',
             'DiamondsJ':'diamonds_J.png',
             'DiamondsQ':'diamonds_Q.png',
             'DiamondsK':'diamonds_K.png',
             'HeartsA':'hearts_A.png', 
             'Hearts2':'hearts_2.png', 
             'Hearts3':'hearts_3.png',
             'Hearts4':'hearts_4.png',
             'Hearts5':'hearts_5.png',
             'Hearts6':'hearts_6.png', 
             'Hearts7':'hearts_7.png',
             'hearts8':'hearts_8.png',
             'Hearts9':'hearts_9.png',
             'Hearts10':'hearts_10.png',
             'HeartsJ':'hearts_J.png',
             'HeartsQ':'hearts_Q.png',
             'HeartsK':'hearts_K.png',
             'ClubsA':'clubs_A.png', 
             'Clubs2':'clubs_2.png', 
             'Clubs3':'clubs_3.png',
             'Clubs4':'clubs_4.png',
             'Clubs5':'clubs_5.png',
             'Clubs6':'clubs_6.png', 
             'Clubs7':'clubs_7.png',
             'Clubs8':'clubs_8.png',
             'Clubs9':'clubs_9.png',
             'Clubs10':'clubs_10.png',
             'ClubsJ':'clubs_J.png',
             'ClubsQ':'clubs_Q.png',
             'ClubsK':'clubs_K.png'
            }

@app.route('/card', methods=['POST'])
def card():
    cards = request.get_json()
    symbol = cards["symbol"]
    suit = cards["suit"]
    card_image_key = suit+symbol
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