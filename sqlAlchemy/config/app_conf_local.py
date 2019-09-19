import os
from ast import literal_eval
_basedir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'../sqlAlchemy/models/test.db')

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', "sqlite:///"+ path)
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

