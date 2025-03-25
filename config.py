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

    # Email to handling errors.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None  # Enxrypted conn
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['pedronovaesmelo@gmail.com']
