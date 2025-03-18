"""Module to store web form classes."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember_me = BooleanField(label='Remember me')
    submit = SubmitField(label='Sign in')


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password2 = PasswordField(
        label='Repeat Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField(label='Register')

    def validate_username(self, username):
        user = db.session.scalar(
            sa
            .select(User)
            .where(User.username == username.data)
        )

        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(
            sa
            .select(User)
            .where(User.email == email.data)
        )

        if user is not None:
            raise ValidationError('Please use a different email address.')
