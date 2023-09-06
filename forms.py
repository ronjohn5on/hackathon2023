from wtforms import Form, StringField, PasswordField, validators, EmailField, SelectField
from wtforms.validators import Email, EqualTo, DataRequired, Length

class Login(Form):
    Username = StringField("",[validators.Length(min=1, max=100), validators.DataRequired()])
    Password = PasswordField('', [validators.Length(min=8, max=15, message="Error"), validators.DataRequired()])

class quiz(Form):
    qn1 = SelectField('please select',choices=[('t1','test1'),('t2','test2'),('t3','test3')], validators=[DataRequired()] )

class bmi(Form):
    weight = StringField("Input your weight in Kg",[validators.Length(min=1, max=10), validators.DataRequired()])
    height = StringField("Input your height in cm",[validators.Length(min=1, max=10), validators.DataRequired()])