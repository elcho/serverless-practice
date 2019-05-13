import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # DEBUG = os.getenv('DEBUG', False)
    # SECRET_KEY = os.getenv('SECRET_KEY', '4jOvmMvhUBFU_5iLbpY2Wk7a-HQGZuZdrt5zJveS9Dc=')
    # SESSION_TYPE = os.getenv('SESSION_TYPE', 'filesystem')
    FLASK_ENV = os.getenv('FLASK_ENV')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # AES_SECRET_KEY = os.getenv('AES_SECRET_KEY')
