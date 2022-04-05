from application import db

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cards_value = db.Column(db.String(50))
    cards_suit = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime)

    def __str__(self):
        return f"{self.cards_value} of {self.cards_suit}"