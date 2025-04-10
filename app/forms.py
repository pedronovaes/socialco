"""Module to store web form classes."""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    EqualTo,
    Length
)

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


class EditProfileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    about_me = TextAreaField(label='About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    # Overload constructor that accepts the original username as an argument.
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        # If the username entered by the user in the form is the same as the
        # original username, then there is no reason to check the database for
        # duplicates.
        if username.data != self.original_username:
            user = db.session.scalar(
                sa
                .select(User)
                .where(User.username == username.data)
            )

            if user is not None:
                raise ValidationError('Please use a different username.')
