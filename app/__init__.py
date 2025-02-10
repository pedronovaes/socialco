from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(obj=Config)

from app import routes
