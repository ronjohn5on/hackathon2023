from app import db

class TestResults(db.Model):
    __tablename__ = 'test_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(20), nullable=False)
    diet = db.Column(db.String(20), nullable=False)
    cuisine = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)


    def __init__(self, time, diet, cuisine, category):
        self.time = time
        self.diet = diet
        self.cuisine = cuisine
        self.category = category
