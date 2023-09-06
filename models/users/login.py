from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Enter a valid email address. (e.g. John@gmail.com)")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')