from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(obj=Config)

db = SQLAlchemy(app=app)  # Database.
migrate = Migrate(app=app, db=db)  # Database migration engine.

from app import routes, models
