"""Module to store configuration variables."""

import os


class Config:
    # Flask and some of its extensions use the value of the secret key as a
    # cryptographic key, useful to generate signatures or tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
