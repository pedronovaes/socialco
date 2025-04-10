import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

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

# Create error handler.
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None

        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

        secure = None

        if app.config['MAIL_USE_TLS']:
            secure = ()

        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Social.co Failure',
            credentials=auth,
            secure=secure
        )

        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(hdlr=mail_handler)

    # File-based log.
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler(
        filename='logs/socialco.log',
        maxBytes=10240,
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Social.co startup')

from app import routes, models, errors
