from app import db

class TestResults(db.Model):
    __tablename__ = 'test_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(20), nullable=False)
    diet = db.Column(db.String(20), nullable=False)
    cuisine = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    goal1 = db.Column(db.String(120), default=None)
    goal2 = db.Column(db.String(120), default=None)
    goal3 = db.Column(db.String(120), default=None)


    def __init__(self, time, diet, cuisine, category, goal1=None, goal2=None, goal3=None):
        self.time = time
        self.diet = diet
        self.cuisine = cuisine
        self.category = category
        self.goal1 = goal1
        self.goal2 = goal2
        self.goal3 = goal3
