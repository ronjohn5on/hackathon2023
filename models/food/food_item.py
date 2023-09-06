from app import db

class ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredient_name = db.Column(db.String(120))

class food_category(db.Model):
    __tablename__ = 'food_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(120))

class food(db.Model):
    __tablename__ = 'food'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable = False)
    cooking_time = db.Column(db.Integer, nullable=False)
    ingredient = db.Column(db.Integer, db.ForeignKey(ingredient.id), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey(food_category.id), nullable=False)
    goal1 = db.Column(db.String(120), default=None)
    goal2 = db.Column(db.String(120), default=None)
    goal3 = db.Column(db.String(120), default=None)
    image = db.Column(db.String(200), default=None)

    ingredients = db.relationship('ingredient', backref='food', lazy=True)
    categories = db.relationship('food_category', backref='food', lazy=True)
