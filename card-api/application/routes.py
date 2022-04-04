from application import app
from flask import request, jsonify

card_deck = {'SpadesA':'/cards/Spades/A.png',
             'Spades2':'/cards/Spades/2.png',
             'Spades3':'/cards/Spades/3.png',
             'Spades4':'/cards/Spades/4.png',
             'Spades5':'/cards/Spades/5.png',
             'Spades6':'/cards/Spades/6.png',
             'Spades7':'/cards/Spades/7.png',
             'Spades8':'/cards/Spades/8.png',
             'Spades9':'/cards/Spades/9.png',
             'Spades10':'/cards/Spades/10.png',
             'SpadesJ':'/cards/Spades/J.png',
             'SpadesQ':'/cards/Spades/Q.png',
             'SpadesK':'/cards/Spades/K.png',
             'HeartsA':'/cards/Hearts/A.png',
             'Hearts2':'/cards/Hearts/2.png',
             'Hearts3':'/cards/Hearts/3.png',
             'Hearts4':'/cards/Hearts/4.png',
             'Hearts5':'/cards/Hearts/5.png',
             'Hearts6':'/cards/Hearts/6.png',
             'Hearts7':'/cards/Hearts/7.png',
             'Hearts8':'/cards/Hearts/8.png',
             'Hearts9':'/cards/Hearts/9.png',
             'Hearts10':'/cards/Hearts/10.png',
             'HeartsJ':'/cards/Hearts/J.png',
             'HeartsQ':'/cards/Hearts/Q.png',
             'HeartsK':'/cards/Hearts/K.png',
             'DiamondsA':'/cards/Diamonds/A.png',
             'Diamonds2':'/cards/Diamonds/2.png',
             'Diamonds3':'/cards/Diamonds/3.png',
             'Diamonds4':'/cards/Diamonds/4.png',
             'Diamonds5':'/cards/Diamonds/5.png',
             'Diamonds6':'/cards/Diamonds/6.png',
             'Diamonds7':'/cards/Diamonds/7.png',
             'Diamonds8':'/cards/Diamonds/8.png',
             'Diamonds9':'/cards/Diamonds/9.png',
             'Diamonds10':'/cards/Diamonds/10.png',
             'DiamondsJ':'/cards/Diamonds/J.png',
             'DiamondsQ':'/cards/Diamonds/Q.png',
             'DiamondsK':'/cards/Diamonds/K.png',
             'ClubsA':'/cards/Clubs/A.png',
             'Clubs2':'/cards/Clubs/2.png',
             'Clubs3':'/cards/Clubs/3.png',
             'Clubs4':'/cards/Clubs/4.png',
             'Clubs5':'/cards/Clubs/5.png',
             'Clubs6':'/cards/Clubs/6.png',
             'Clubs7':'/cards/Clubs/7.png',
             'Clubs8':'/cards/Clubs/8.png',
             'Clubs9':'/cards/Clubs/9.png',
             'Clubs10':'/cards/Clubs/10.png',
             'ClubsJ':'/cards/Clubs/J.png',
             'ClubsQ':'/cards/Clubs/Q.png',
             'ClubsK':'/cards/Clubs/K.png'
            }

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