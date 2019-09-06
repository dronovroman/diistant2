import os
from logging.handlers import RotatingFileHandler
import logging
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_FILEPATH = os.getenv('BASE_FILEPATH')
    LOG_FILENAME = os.getenv('LOG_FILENAME')

    @classmethod
    def init_app(cls, app):
        # Set up logging
        if not os.path.exists(cls.BASE_FILEPATH + 'logs'):
            os.mkdir(cls.BASE_FILEPATH + 'logs')
        if not os.path.exists(cls.BASE_FILEPATH + 'logs/' + cls.LOG_FILENAME):
            open((cls.BASE_FILEPATH + 'logs/' + cls.LOG_FILENAME), 'w').close()
        file_handler = RotatingFileHandler(('logs/' + cls.LOG_FILENAME), maxBytes=10485760, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s [FUNC:%(funcName)s '
                                                    'LINE:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info("################################ A P P   R E B O O T ################################")
