from application import app
from flask import request, jsonify

card_deck = {'SpadesA':'/card-api/application/static/spades_A.png',
             'Spades2':'/card-api/application/static/spades_2.png', 
             'Spades3':'/card-api/application/static/spades_3.png',
             'Spades4':'/card-api/application/static/spades_4.png',
             'Spades5':'/card-api/application/static/spades_5.png',
             'Spades6':'/card-api/application/static/spades_6.png', 
             'Spades7':'/card-api/application/static/spades_7.png',
             'Spades8':'/card-api/application/static/spades_8.png',
             'Spades9':'/card-api/application/static/spades_9.png',
             'Spades10':'/card-api/application/static/spades_10.png',
             'SpadesJ':'/card-api/application/static/spades_J.png',
             'SpadesQ':'/card-api/application/static/spades_Q.png',
             'SpadesK':'/card-api/application/static/spades_K.png', 
             'DiamondsA':'/card-api/application/static/diamonds_A.png', 
             'Diamonds2':'/card-api/application/static/diamonds_2.png', 
             'Diamonds3':'/card-api/application/static/diamonds_3.png',
             'Diamonds4':'/card-api/application/static/diamonds_4.png',
             'Diamonds5':'/card-api/application/static/diamonds_5.png',
             'Diamonds6':'/card-api/application/static/diamonds_6.png', 
             'Diamonds7':'/card-api/application/static/diamonds_7.png',
             'Diamonds8':'/card-api/application/static/diamonds_8.png',
             'Diamonds9':'/card-api/application/static/diamonds_9.png',
             'Diamonds10':'/card-api/application/static/diamonds_10.png',
             'DiamondsJ':'/card-api/application/static/diamonds_J.png',
             'DiamondsQ':'/card-api/application/static/diamonds_Q.png',
             'DiamondsK':'/card-api/application/static/diamonds_K.png',
             'HeartsA':'/card-api/application/static/hearts_A.png', 
             'Hearts2':'/card-api/application/static/hearts_2.png', 
             'Hearts3':'/card-api/application/static/hearts_3.png',
             'Hearts4':'/card-api/application/static/hearts_4.png',
             'Hearts5':'/card-api/application/static/hearts_5.png',
             'Hearts6':'/card-api/application/static/hearts_6.png', 
             'Hearts7':'/card-api/application/static/hearts_7.png',
             'hearts8':'/card-api/application/static/hearts_8.png',
             'Hearts9':'/card-api/application/static/hearts_9.png',
             'Hearts10':'/card-api/application/static/hearts_10.png',
             'HeartsJ':'/card-api/application/static/hearts_J.png',
             'HeartsQ':'/card-api/application/static/hearts_q.png',
             'HeartsK':'/card-api/application/static/hearts_K.png',
             'ClubsA':'/card-api/application/static/clubs_A.png', 
             'Clubs2':'/card-api/application/static/clubs_2.png', 
             'Clubs3':'/card-api/application/static/clubs3.png',
             'Clubs4':'/card-api/application/static/clubs_4.png',
             'Clubs5':'/card-api/application/static/clubs_5.png',
             'Clubs6':'/card-api/application/static/clubs_6.png', 
             'Clubs7':'/card-api/application/static/clubs_7.png',
             'Clubs8':'/card-api/application/static/clubs_8.png',
             'Clubs9':'/card-api/application/static/clubs_9.png',
             'Clubs10':'/card-api/application/static/clubs_10.png',
             'ClubsJ':'/card-api/application/static/clubs_J.png',
             'ClubsQ':'/card-api/application/static/clubs_Q.png',
             'ClubsK':'/card-api/application/static/clubs_k.png'}

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