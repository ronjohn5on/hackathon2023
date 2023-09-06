from wtforms import Form, StringField, PasswordField, validators, EmailField, SelectField, widgets, SelectMultipleField
from wtforms.validators import Email, EqualTo, DataRequired, Length
from flask_wtf import FlaskForm

class Login(Form):
    Username = StringField("",[validators.Length(min=1, max=100), validators.DataRequired()])
    Password = PasswordField('', [validators.Length(min=8, max=15, message="Error"), validators.DataRequired()])

class quiz(FlaskForm):
    time = SelectField('Cooking time',choices=[('<20mins','<20mins'),('<30mins','<30mins'),('<1h','<1h'),('>1h','>1h')], validators=[DataRequired()] )
    diet = SelectField('Dietery restrictions',choices=[('veg','Vegetarian'),('hal','Halal'),('NIL','NIL')], validators=[DataRequired()] )
    cuisine = SelectField('Which cuisine',choices=[('ws','western'),('ch','chinese'),], validators=[DataRequired()] )
    category = SelectField('Category of food',choices=[('bf','breakfast'),('lu','lunch'),('dn','dinner')], validators=[DataRequired()] )
    # Define the 'Goals' field as a SelectMultipleField
    goals = SelectMultipleField('Goals', choices=[
            ('Maximum Nutrition Meal', 'Maximum Nutrition Meal'),
            ('Weightless Meal', 'Weightless Meal'),
            ('Protein Meal', 'Protein Meal')
        ], validators=[DataRequired()])

class bmi(Form):
    weight = StringField("Input your weight in Kg",[validators.Length(min=1, max=10), validators.DataRequired()])
    height = StringField("Input your height in cm",[validators.Length(min=1, max=10), validators.DataRequired()])