from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import current_user, LoginManager, UserMixin, login_user, logout_user, login_required
from app import *
from models.users.login import LoginForm
from models.users.register import RegistrationForm, ProfileForm
from models.users.users import Users
from models.food.food_item import food, ingredient, food_category
from models.favourite.favourite import Favourites
from sqlalchemy import func, desc
import random
import string
from forms import *
from flask_session import Session
import bcrypt



login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = '!QAZ@WSX#EDC$RFV%TGB'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)  # Set session timeout to 30 minutes
Session(app)

DEFAULT_PROFILE_PICTURE = "Placeholder.png"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Function to generate a random token
def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

@app.route('/')
@app.route('/home')
def home():
    if not session.get('logged_in'):
        pass
        #return redirect(url_for('register'))

    try:
        #get all the question answer here by logged username
        pass
    except Exception as e:
        return 'Error occurred,', e
    else:
        pass
        #Get all the food item
        #SELECT * FROM diet_plan WHERE 'requirement' = answer




    return render_template('home.html')


@app.route('/favouriteHandler/<int:food_id>')
def favouriteHandler(food_id):
    if not session.get('logged_in'):
        return redirect(url_for('register'))

    try:
        food_item = food.query.filter_by(id=food_id).first()
    except Exception as e:
        print("Error has occured,"), e
    else:
        #if food item exist

        #Get the account id
        account_id = Users.query.filter_by(username=session.get('username')).first().id

        # Check that the food is not already favourited
        favourited_questionmark = Favourites.query.filter_by(account_id_foreign_key=account_id, food_id_foreign_key=food_id).first()

        if not favourited_questionmark:
            newFavourite = Favourites(account_id_foreign_key=account_id, food_id_foreign_key=food_id) #Adding new favourite
            # Add the new user to the database
            db.session.add(newFavourite)
            db.session.commit()
            return 'new favourited'
        else:
            return 'this item already favourited'

    return 'not favourited'

@app.route('/favourite') #Show favourite
def favourite():
    if not session.get('logged_in'):
        return redirect(url_for('register'))

    try:
        account_id = Users.query.filter_by(username=session.get('username')).first().id
        favourites = Favourites.query.filter_by(account_id_foreign_key=account_id).all()
    except Exception as e:
        return e
    else:
        all_food = []
        for data in favourites:
            all_food.append(data.food_id_foreign_key)
        print(all_food)
    return 'Favourite page'


@app.route('/bmi')
def bmiCal():
    form = bmi()
    return render_template('bmi.html')

# Account Management
@app.route('/register', methods=['GET', 'POST'])
def register():

    if session.get('logged_in'):
        return redirect('/home')

    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        profile_picture = DEFAULT_PROFILE_PICTURE

        token = generate_token()

        # Check if user with the same email already exists
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            flash('Email/Username already exists. Please choose a different email/username.', category='alert-danger')
            return redirect(url_for('register'))

        # Check if user with the same username already exists
        existing_user_username = Users.query.filter_by(username=username).first()
        if existing_user_username:
            flash('Email/Username already exists. Please choose a different email/username.', category='alert-danger')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user object
        new_user = Users(email=email, username=username, password=hashed_password, profile_picture=profile_picture)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please verify your email before logging in!', category='alert-success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('logged_in'):
        return redirect('/home')

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Fetch the user from the database based on the provided email
        user = Users.query.filter_by(email=email).first()

        if user:
                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    # Authentication successful, perform login
                    # You can use session or Flask-Login for user session management

                    login_user(user)  # Set the user in the session
                    session['username'] = user.username
                    session['logged_in'] = True
                    flash('Login successful!', category='alert-success')
                    next_page = request.args.get('next') or url_for('home')


                    if next_page == url_for('home'):
                        return redirect(url_for('home'))
                    # return redirect(next_page)
                else:
                    flash('Invalid credentials.', category='alert-danger')
                    return redirect(url_for('login'))
        else:
            flash('Invalid credentials.', category='alert-danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)






@app.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    logout_user()
    flash('You have been logged out.', category='alert-success')
    return redirect(url_for('home'))

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.errorhandler(404)
def url_error(error):
    return render_template('404error.html'),404

@app.errorhandler(Exception)
def internal_error(error):
    print(f'user has {error}')
    return render_template('500error.html'),500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)