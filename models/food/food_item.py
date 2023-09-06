from app import db

class food(db.Model):
    __tablename__ = 'food'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable = False)
    cooking_time = db.Column(db.Integer, nullable=False)
    goal1 = db.Column(db.String(120), default=None)
    goal2 = db.Column(db.String(120), default=None)
    goal3 = db.Column(db.String(120), default=None)

class ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_id_foreign_key = db.Column(db.Integer)
    ingredient_name = db.Column(db.String(120))

class food_category(db.Model):
    __tablename__ = 'food_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_id_foreign_key = db.Column(db.Integer)
    category = db.Column(db.String(120))

