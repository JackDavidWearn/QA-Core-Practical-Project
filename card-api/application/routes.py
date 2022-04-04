from application import app
from flask import request, jsonify

card_deck = {'SpadesA':'/card-api/application/cards/Spades/A.png',
             'Spades2':'/card-api/application/cards/Spades/2.png',
             'Spades3':'/card-api/application/cards/Spades/3.png',
             'Spades4':'/card-api/application/cards/Spades/4.png',
             'Spades5':'/card-api/application/cards/Spades/5.png',
             'Spades6':'/card-api/application/cards/Spades/6.png',
             'Spades7':'/card-api/application/cards/Spades/7.png',
             'Spades8':'/card-api/application/cards/Spades/8.png',
             'Spades9':'/card-api/application/cards/Spades/9.png',
             'Spades10':'/card-api/application/cards/Spades/10.png',
             'SpadesJ':'/card-api/application/cards/Spades/J.png',
             'SpadesQ':'/card-api/application/cards/Spades/Q.png',
             'SpadesK':'/card-api/application/cards/Spades/K.png',
             'HeartsA':'/card-api/application/cards/Hearts/A.png',
             'Hearts2':'/card-api/application/cards/Hearts/2.png',
             'Hearts3':'/card-api/application/cards/Hearts/3.png',
             'Hearts4':'/card-api/application/cards/Hearts/4.png',
             'Hearts5':'/card-api/application/cards/Hearts/5.png',
             'Hearts6':'/card-api/application/cards/Hearts/6.png',
             'Hearts7':'/card-api/application/cards/Hearts/7.png',
             'Hearts8':'/card-api/application/cards/Hearts/8.png',
             'Hearts9':'/card-api/application/cards/Hearts/9.png',
             'Hearts10':'/card-api/application/cards/Hearts/10.png',
             'HeartsJ':'/card-api/application/cards/Hearts/J.png',
             'HeartsQ':'/card-api/application/cards/Hearts/Q.png',
             'HeartsK':'/card-api/application/cards/Hearts/K.png',
             'DiamondsA':'/card-api/application/cards/Diamonds/A.png',
             'Diamonds2':'/card-api/application/cards/Diamonds/2.png',
             'Diamonds3':'/card-api/application/cards/Diamonds/3.png',
             'Diamonds4':'/card-api/application/cards/Diamonds/4.png',
             'Diamonds5':'/card-api/application/cards/Diamonds/5.png',
             'Diamonds6':'/card-api/application/cards/Diamonds/6.png',
             'Diamonds7':'/card-api/application/cards/Diamonds/7.png',
             'Diamonds8':'/card-api/application/cards/Diamonds/8.png',
             'Diamonds9':'/card-api/application/cards/Diamonds/9.png',
             'Diamonds10':'/card-api/application/cards/Diamonds/10.png',
             'DiamondsJ':'/card-api/application/cards/Diamonds/J.png',
             'DiamondsQ':'/card-api/application/cards/Diamonds/Q.png',
             'DiamondsK':'/card-api/application/cards/Diamonds/K.png',
             'ClubsA':'/card-api/application/cards/Clubs/A.png',
             'Clubs2':'/card-api/application/cards/Clubs/2.png',
             'Clubs3':'/card-api/application/cards/Clubs/3.png',
             'Clubs4':'/card-api/application/cards/Clubs/4.png',
             'Clubs5':'/card-api/application/cards/Clubs/5.png',
             'Clubs6':'/card-api/application/cards/Clubs/6.png',
             'Clubs7':'/card-api/application/cards/Clubs/7.png',
             'Clubs8':'/card-api/application/cards/Clubs/8.png',
             'Clubs9':'/card-api/application/cards/Clubs/9.png',
             'Clubs10':'/card-api/application/cards/Clubs/10.png',
             'ClubsJ':'/card-api/application/cards/Clubs/J.png',
             'ClubsQ':'/card-api/application/cards/Clubs/Q.png',
             'ClubsK':'/card-api/application/cards/Clubs/K.png'
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
    
    
    # card_json = request.get_json()
    # card_value = card_json["value"]
    # card_suit = card_json["suit"]
    # if card_value == 'Joker':
    #     return f'{card_value}, the unlucky {card_suit}'
    # elif card_suit == 'Joker':
    #     return f'{card_value}, the unlucky {card_suit}'
    # else:
    #     return f'{card_value} of {card_suit}'