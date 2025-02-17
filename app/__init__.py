from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(obj=Config)

db = SQLAlchemy(app=app)  # Database.
migrate = Migrate(app=app, db=db)  # Database migration engine.

login = LoginManager(app=app)  # Login initialization.
login.login_view = 'login'  # Forces users to log in before view certain pages.

from app import routes, models
