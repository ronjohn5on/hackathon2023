import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
#from flask_socketio import SocketIO
#from flask_jwt_extended import JWTManager
#from twilio.rest import Client

app = Flask(__name__)
#socketio = SocketIO(app, cors_allowed_origins="*")

# mysql_database with sqlalchemy
password = urllib.parse.quote_plus('wenjie') # replace with your password
uri = f"mysql+pymysql://root:{password}@localhost/nutriguide"
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config["SECRET_KEY"] = "xxkxcZKH2TxsSw7bew8D9gLpCaa3YYnn"
db = SQLAlchemy(app)