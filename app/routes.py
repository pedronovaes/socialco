"""
This module handles several routes that social.co supports using view
functions.
"""

from urllib.parse import urlsplit
from datetime import datetime, timezone

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

import sqlalchemy as sa

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
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


@app.route('/register', methods=['GET', 'POST'])
def register():

    # Check if user is already authenticated.
    if current_user.is_authenticated:
        return redirect(location=url_for('index'))

    form = RegistrationForm()

    # All form processing work (receiving registration data).
    if form.validate_on_submit():

        # Create and commit new user into database.
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(password=form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user on Social.co!')

        return redirect(location=url_for('login'))

    return render_template(
        template_name_or_list='register.html',
        title='Register',
        form=form
    )


@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))

    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]

    return render_template('user.html', user=user, posts=posts)


# Using this decorator allows to execute any code before any view function in
# the application.
@app.before_request
def before_request():

    # Check if user is authenticated.
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(tz=timezone.utc)
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    # Form processing work.
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data

        db.session.commit()

        flash('Your changes have been saved.')

        return redirect(location=url_for('edit_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template(
        template_name_or_list='edit_profile.html',
        title='Edit Profile',
        form=form
    )
