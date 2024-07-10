# The routes module handle the different URLs that the application supports.
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pedro'}
    posts = [
        {'author': {'username': 'Pedro'}, 'body': 'Lindo dia em Monte Verde!'},
        {'author': {'username': 'Carol'}, 'body': 'O Corinthians é o mundo!'},
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
