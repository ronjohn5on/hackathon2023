from wtforms import Form, StringField, PasswordField, validators, EmailField, SelectField

class Login(Form):
    Username = StringField("",[validators.Length(min=1, max=100), validators.DataRequired()])
    Password = PasswordField('', [validators.Length(min=8, max=15, message="Error"), validators.DataRequired()])