from app import app
from flask import render_template

# Fake content
posts = [
    {
        'author': 'Pedro Marcelino',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 28, 2021'
    },
    {
        'author': 'Carol Fernandes',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 29, 2021'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')
