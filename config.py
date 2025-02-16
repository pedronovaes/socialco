"""Module to store configuration variables."""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask and some of its extensions use the value of the secret key as a
    # cryptographic key, useful to generate signatures or tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Location fo the application's database.
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL')
        or
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
