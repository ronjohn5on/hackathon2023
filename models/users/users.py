from app import db

class Users(db.Model):
    __tablename__ = 'Users'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable =False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_charity_manager = db.Column(db.Boolean, default=False)
    verified = db.Column(db.Boolean, default=False)
    reset_token = db.Column(db.String(100))
    reset_token_expiration = db.Column(db.DateTime)
    verification_token = db.Column(db.String(100))
    verification_token_expiration = db.Column(db.DateTime)
    profile_picture = db.Column(db.String(200))  # Add the profile picture column
    totp_secret_key = db.Column(db.String(1000))
    totp_secret_key_iv = db.Column(db.String(1000))
    user_cart = db.Column(db.PickleType, default = {})

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
    
    def get_phone_number(self):
        return str(self.phone_number)

    def get_email(self):
        return str(self.email)