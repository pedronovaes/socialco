import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '5c2ab8adf5a6b725eb876f2c3638140c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///socialco.db'
