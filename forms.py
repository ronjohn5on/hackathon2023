from wtforms import Form, StringField, PasswordField, validators, EmailField, SelectField
from wtforms.validators import Email, EqualTo, DataRequired, Length
from flask_wtf import FlaskForm

class Login(Form):
    Username = StringField("",[validators.Length(min=1, max=100), validators.DataRequired()])
    Password = PasswordField('', [validators.Length(min=8, max=15, message="Error"), validators.DataRequired()])

class quiz(FlaskForm):
    time = SelectField('Cooking time',choices=[('>20mins','>20mins'),('>30mins','>30mins'),('>1h','>1h')], validators=[DataRequired()] )
    diet = SelectField('Dietery restrictions',choices=[('Vegetarian','Vegetarian'),('hal','Halal'),], validators=[DataRequired()] )
    cuisine = SelectField('Which cuisine',choices=[('western','western'),('chinese','chinese'),], validators=[DataRequired()] )
    category = SelectField('Category of food',choices=[('breakfast','breakfast'),('lunch','lunch'),('dinner','dinner')], validators=[DataRequired()] )

class bmi(Form):
    weight = StringField("Input your weight in Kg",[validators.Length(min=1, max=10), validators.DataRequired()])
    height = StringField("Input your height in cm",[validators.Length(min=1, max=10), validators.DataRequired()])