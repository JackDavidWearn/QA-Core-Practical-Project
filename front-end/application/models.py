from application import db

class Cards(db.Model):

    pk_cards_id = db.Column(db.Integer, primary_key=True)
    cards_value = db.Column(db.String(50))
    cards_suit = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.cards_value} of {self.cards_suit}"