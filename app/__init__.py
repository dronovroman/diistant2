from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Global variables
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'


def create_app():
    app = Flask(__name__)

    with app.app_context():

        app.config.from_object(Config)
        Config.init_app(app=app)

        db.init_app(app=app)
        login.init_app(app=app)

        return app
