"""
This module handles several routes that social.co supports using view
functions.
"""

from urllib.parse import urlsplit

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

import sqlalchemy as sa

from app import app, db
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
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
        posts=posts
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """View function to login a user."""

    # Check if user is already authenticated.
    if current_user.is_authenticated:
        return redirect(location=url_for('index'))

    form = LoginForm()

    # All form processing work (receiving login credentials and so on).
    if form.validate_on_submit():

        # Load user from database..
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )

        if user is None or not user.check_password(password=form.password.data):
            flash('Invalid username or password')

            return redirect(location=url_for('login'))

        login_user(user=user, remember=form.remember_me.data)  # Login success!

        # Check if user will be redirect to other page than index.
        next_page = request.args.get('next')
        if not next_page or urlsplit(url=next_page).netloc != '':
            next_page = url_for('index')

        return redirect(location=next_page)

    # Executes when the browser sends the GET request to receive the web page
    # with the form.
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()

    return redirect(location=url_for('index'))
