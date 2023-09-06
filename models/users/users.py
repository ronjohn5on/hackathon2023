from app import db

class Users(db.Model):
    __tablename__ = 'Users'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable =False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    profile_picture = db.Column(db.String(200))  # Add the profile picture column

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