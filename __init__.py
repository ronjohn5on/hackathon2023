from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



@app.errorhandler(404)
def url_error():
    return render_template('404error.html'),404

@app.errorhandler(Exception)
def internal_error(error):
    print(f'user has {error}')
    return render_template('500error.html'),500

if __name__ == '__main__':
    app.run(debug=True)