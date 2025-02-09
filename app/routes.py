"""
This module handles several routes that social.co supports using view fucntions.
"""

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pedro'}
    posts = [
        {
            'author': {'username': 'Carol'},
            'body': 'Lindo dia em João Dourado!'
        },
        {
            'author': {'username': 'Hamilton'},
            'body': 'Pilotarei pela Ferrari em 2025 :)'
        }
    ]

    # Invokes Jinja template engine to render index.html page.
    return render_template(
        template_name_or_list='index.html',
        title='Home',
        user=user,
        posts=posts
    )
