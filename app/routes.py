"""
This module handles several routes that social.co supports using view
functions.
"""

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    """View function to login a user."""

    form = LoginForm()

    # All form processing work (receiving login credentials and so on).
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')

        return redirect(location='/index')

    # Executes when the browser sends the GET request to receive the web page
    # with the form.
    return render_template('login.html', title='Sign In', form=form)
