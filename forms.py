from wtforms import Form, StringField, PasswordField, validators, EmailField, SelectField
from wtforms.validators import Email, EqualTo, DataRequired, Length

class Login(Form):
    Username = StringField("",[validators.Length(min=1, max=100), validators.DataRequired()])
    Password = PasswordField('', [validators.Length(min=8, max=15, message="Error"), validators.DataRequired()])

class quiz(Form):
    time = SelectField('Cooking time',choices=[('>20mins','>20mins'),('>30mins','>30mins'),('>1h','>1h')], validators=[DataRequired()] )
    diet = SelectField('Dietery restrictions',choices=[('veg','vegetarian'),('hal','malay'),], validators=[DataRequired()] )
    cuisine = SelectField('Which cuisine',choices=[('ws','western'),('ch','chinese'),], validators=[DataRequired()] )
    category = SelectField('Category of food',choices=[('bf','breakfast'),('lu','lunch'),('dn','dinner')], validators=[DataRequired()] )

class bmi(Form):
    weight = StringField("Input your weight in Kg",[validators.Length(min=1, max=10), validators.DataRequired()])
    height = StringField("Input your height in cm",[validators.Length(min=1, max=10), validators.DataRequired()])