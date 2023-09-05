from flask import Flask, render_template, request, redirect, url_for
from app import *
from models.users.users import Users
from sqlalchemy import func, desc


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



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