from app import db
from models.results.test_results import TestResults

class Users(db.Model):
    __tablename__ = 'Users'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable =False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    profile_picture = db.Column(db.String(200))  # Add the profile picture column
    test_results = db.Column(db.Integer, db.ForeignKey(TestResults.id))

    result = db.relationship(TestResults, backref='result')

    # Implement the UserMixin methods
    def is_active(self):
        return True  # You can modify this method based on your requirements

    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True  # You can modify this method based on your authentication logic

    def get_id(self):
        return str(self.id)
    
    def get_username(self):
        return str(self.username)

    def get_email(self):
        return str(self.email)
    
    # def get_test_results(id):
    #     user = Users.query.get(id)
    #     if user:
    #         return user.result
    #     return None