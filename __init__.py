from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import current_user, LoginManager, UserMixin, login_user, logout_user, login_required
from app import *
from models.users.login import LoginForm
from models.users.register import RegistrationForm, ProfileForm
from models.users.users import Users
from models.food.food_item import food, ingredient, food_category, food_time, food_restriction
from models.favourite.favourite import Favourites
from models.results.test_results import TestResults
from sqlalchemy import func, desc
import random
import string
from forms import *
from flask_session import Session
import bcrypt
from forms import quiz



login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = '!QAZ@WSX#EDC$RFV%TGB'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)  # Set session timeout to 30 minutes
Session(app)

app.config['UPLOAD_FOLDER'] = 'static/img'
DEFAULT_PROFILE_PICTURE = "Placeholder.png"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Function to generate a random token
def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

def create_ingredient():
    with app.app_context():
        existing = ingredient.query.all()
        if not existing:
            ingredient1 = ingredient(ingredient_name="Rice")
            ingredient2 = ingredient(ingredient_name="Noodles")
            db.session.add(ingredient1)
            db.session.add(ingredient2)
            db.session.commit()

def create_food_category():
    with app.app_context():
        existing = food_category.query.all()
        if not existing:
            category1 = food_category(category="Western")
            category2 = food_category(category="Chinese")
            db.session.add(category1)
            db.session.add(category2)
            db.session.commit()

def create_food_time():
     with app.app_context():
        existing = food_time.query.all()
        if not existing:
            time1 = food_time(time="Breakfast")
            time2 = food_time(time="Lunch")
            time3 = food_time(time="Dinner")
            db.session.add(time1)
            db.session.add(time2)
            db.session.add(time3)
            db.session.commit()

def create_food_restriction():
     with app.app_context():
        existing = food_restriction.query.all()
        if not existing:
            restriction1 = food_restriction(restriction="Vegetarian")
            restriction2 = food_restriction(restriction="Halal")
            restriction3 = food_restriction(restriction="NIL")
            db.session.add(restriction1)
            db.session.add(restriction2)
            db.session.add(restriction3)
            db.session.commit()

def create_food_time():
     with app.app_context():
        existing = food_time.query.all()
        if not existing:
            time1 = food_time(time="Breakfast")
            time2 = food_time(time="Lunch")
            time3 = food_time(time="Dinner")
            db.session.add(time1)
            db.session.add(time2)
            db.session.add(time3)
            db.session.commit()

def create_food():
    with app.app_context():
        existing = food.query.all()
        if not existing:
            food_item1 = food(
                title="Chicken Rice",
                cooking_time=30,
                ingredient = 1,
                category = 2,
                time = 2,
                restriction = 3,
                goal1="Goal 1",
                goal2="Goal 2",
                goal3="Goal 3",
                image = "chicken_rice.webp",
                cooking_direction = '''
                Ingredients:

                For the Chicken:
                - 1 whole chicken (about 3-4 pounds)
                - 1 thumb-sized piece of ginger, peeled and sliced
                - 2-3 cloves garlic, peeled
                - Salt, to taste
                - Water, enough to cover the chicken

                For the Rice:
                - 2 cups jasmine rice (or any long-grain rice)
                - 2 1/2 cups chicken broth (from cooking the chicken)
                - 1 thumb-sized piece of ginger, peeled and minced
                - 2-3 cloves garlic, minced
                - Salt, to taste

                For the Sauce:
                - Soy sauce
                - Sesame oil
                - Chili sauce (optional)

                Instructions:

                1. Rinse the rice under cold water until the water runs clear. Drain and set aside.

                2. In a large pot, bring enough water to a boil to submerge the whole chicken. Add the ginger, garlic, and salt to the boiling water.

                3. Carefully add the whole chicken to the boiling water, breast-side down. Cover the pot, reduce the heat to a simmer, and cook for about 40-50 minutes or until the chicken is fully cooked. You can check for doneness by inserting a knife into the thigh; the juices should run clear.

                4. Once the chicken is cooked, remove it from the pot and place it in a bowl of ice water to cool quickly. This helps to retain the chicken's tenderness and flavor. Once cooled, rub the chicken with a little salt and sesame oil. Set it aside.

                5. While the chicken is cooling, use the chicken broth you cooked the chicken in to prepare the rice. In a separate pot, heat a little vegetable oil and sauté the minced ginger and garlic until fragrant. Add the rice and stir for a couple of minutes.

                6. Pour in the chicken broth, and bring it to a boil. Reduce the heat to low, cover the pot, and simmer for about 15-20 minutes or until the rice is cooked and the liquid is absorbed. Fluff the rice with a fork.

                7. To serve, slice the chicken into bite-sized pieces.

                8. Prepare the dipping sauce by mixing soy sauce, a bit of sesame oil, and chili sauce (if desired) to taste. You can also add some chopped fresh cilantro and green onions for extra flavor.

                9. Serve the sliced chicken on a plate with a side of chicken rice and the dipping sauce.

                Enjoy your homemade chicken rice! This dish is delicious and comforting, with tender chicken and fragrant rice, complemented by the flavorful dipping sauce.
                '''

            )
            food_item2 = food(
                title="Spaghetti",
                cooking_time=10,
                ingredient = 2,
                category = 1,
                time = 1,
                restriction = 3,
                goal1="Goal 1",
                goal2="Goal 2",
                goal3="Goal 3",
                image = "spagehti.jpg",
                cooking_direction='''
                    Ingredients:

                    For the Spaghetti:
                    - 8 ounces (about 1/2 pound) of spaghetti
                    - Salt, for boiling water

                    For the Tomato Sauce:
                    - 1 can (28 ounces) of crushed tomatoes
                    - 2 cloves garlic, minced
                    - 1 small onion, finely chopped
                    - 2 tablespoons olive oil
                    - 1 teaspoon dried basil
                    - 1 teaspoon dried oregano
                    - Salt and pepper, to taste
                    - Red pepper flakes (optional, for heat)
                    - Fresh basil leaves, for garnish (optional)
                    - Grated Parmesan cheese, for topping (optional)

                    Instructions:

                    1. Bring a large pot of salted water to a boil. Add the spaghetti and cook according to the package instructions until al dente. Drain and set aside.

                    2. In a large skillet or saucepan, heat the olive oil over medium heat. Add the minced garlic and chopped onion. Sauté for about 2-3 minutes or until the onion becomes translucent.

                    3. Add the crushed tomatoes to the skillet, along with dried basil, dried oregano, salt, pepper, and red pepper flakes if you like it spicy. Stir to combine.

                    4. Reduce the heat to low and let the sauce simmer for about 15-20 minutes, stirring occasionally. This allows the flavors to meld and the sauce to thicken.

                    5. Taste the sauce and adjust the seasoning as needed.

                    6. To serve, divide the cooked spaghetti among plates, ladle the tomato sauce over the spaghetti, and garnish with fresh basil leaves and grated Parmesan cheese if desired.

                    7. Enjoy your homemade spaghetti with tomato sauce!

                    This classic spaghetti recipe is simple and delicious. You can customize it by adding cooked meatballs, sausages, or vegetables to the sauce if you prefer. Adjust the seasonings to your taste and enjoy!
                    '''

            )
            db.session.add(food_item1)
            db.session.add(food_item2)
            db.session.commit()


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
        else:
            db.session.delete(favourited_questionmark)
            db.session.commit()

    return redirect(request.referrer)


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
        all_favourited = [i.food_id_foreign_key for i in favourites]
        all_food = [i for i in food.query.all() if i.id in all_favourited]
        return render_template('favourite.html', favourited=all_food)


@app.route('/bmi',methods=['GET', 'POST'])
def bmiCal():
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

        # Check if there are quiz choices stored in the session
        quiz_choices = session.get('quiz_choices')
        if quiz_choices:
            # Create a new TestResults record and associate it with the user
            result = TestResults(
                time=quiz_choices['time'],
                diet=quiz_choices['diet'],
                cuisine=quiz_choices['cuisine'],
                category=quiz_choices['category'],
                goal1=quiz_choices['goal1'],
                goal2=quiz_choices['goal2'],
                goal3=quiz_choices['goal3']
            )
            db.session.add(result)
            db.session.commit()

            # Create a new user object
            new_user = Users(email=email, username=username, password=hashed_password, profile_picture=profile_picture, test_results=result.id)
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            # Remove the quiz choices from the session
            session.pop('quiz_choices', None)

        else:
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

@app.route('/food/<int:id>')
def food_details(id):
    try:
        food_item = food.query.filter_by(id=id).first()
    except Exception as e:
        return 'eroror is', e
    else:
        print("Food no error: ", food_item)

        favourite_list = None
        # Get user favourite list
        if session.get('logged_in'):
            account_id = Users.query.filter_by(username=session.get('username')).first().id
            favourite_list = [i.food_id_foreign_key for i in
                              Favourites.query.filter_by(account_id_foreign_key=account_id).all()]
            print(favourite_list)

        return render_template('food_details.html', food_item=food_item, favourite_list=favourite_list)


@app.route('/food_items')
def display_food_items():
    # Query the food table to retrieve all food items
    food_items = food.query.all()
    return render_template('food_items.html', food_items=food_items)



@app.route('/food_items2')
def display_food_items2():
    # Query the food table to retrieve all food items
    food_items = food.query.all()
    favourite_list = None
    #Get user favourite list
    if session.get('logged_in'):
        account_id = Users.query.filter_by(username=session.get('username')).first().id
        favourite_list = [i.food_id_foreign_key for i in Favourites.query.filter_by(account_id_foreign_key=account_id).all()]
        print(favourite_list)
    return render_template('food_items2.html', food_items=food_items, favourite_list=favourite_list)

@app.route('/quiz',methods=['GET', 'POST'])
def quizPage():
    form = quiz()

    if form.validate_on_submit():
        selected_goals = form.goals.data
        goal1 = None
        goal2 = None
        goal3 = None
        
        if len(selected_goals) >= 1:
            goal1 = selected_goals[0]
        if len(selected_goals) >= 2:
            goal2 = selected_goals[1]
        if len(selected_goals) >= 3:
            goal3 = selected_goals[2]
    
        # Process the form data and save it to the database (replace with your logic)
        if current_user.is_authenticated:
            result = TestResults(
                time=form.time.data,
                diet=form.diet.data,
                cuisine=form.cuisine.data,
                category=form.category.data,
                goal1=goal1,
                goal2=goal2,
                goal3=goal3
            )
            
            db.session.add(result)
            db.session.commit()
            current_user.test_results = result.id
            db.session.commit()
            flash('Quiz submitted successfully!', 'success')
            return redirect(url_for('home'))
        else:
            session['quiz_choices'] = {
                'time': form.time.data,
                'diet': form.diet.data,
                'cuisine': form.cuisine.data,
                'category': form.category.data,
                'goal1': goal1,
                'goal2': goal2,
                'goal3': goal3
            }
            print(session['quiz_choices'])
            flash('Quiz submitted successfully!', 'success')
            return redirect(url_for('home'))

    return render_template('quiz.html', form=form)

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
        create_ingredient()
        create_food_category()
        create_food_time()
        create_food_restriction()
        create_food()
    app.run(debug=True)
