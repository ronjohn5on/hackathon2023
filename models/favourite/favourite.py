from app import db

class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id_foreign_key = db.Column(db.Integer)
    food_id_foreign_key = db.Column(db.Integer)
