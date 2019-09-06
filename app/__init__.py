from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Global variables
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'


def create_app(config_name):
    app = Flask(__name__)

    with app.app_context():

        app.config.from_object(config[config_name])
        config[config_name].init_app(app=app)

        db.init_app(app=app)
        login.init_app(app=app)

        return app
