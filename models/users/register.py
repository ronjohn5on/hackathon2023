from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_]).{8,}$", message='Minimum eight characters, at least one uppercase, one lowercase letter, one number and one special character.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords are not equal.')])
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):
    profile_picture = FileField('Profile Picture')
    submit = SubmitField('Update')