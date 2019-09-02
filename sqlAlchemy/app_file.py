import sys
import os
sys.path.append("C:\\Users\\ramesh.kg\\PycharmProjects\\sqlAlchemy\\")
from flask import Flask
from sqlAlchemy.apis import api
from sqlAlchemy.models.utils.base_db import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
path = os.path.abspath(os.path.dirname(__file__))+'\\models\\test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\\\Users\\\\ramesh.kg\\\\PycharmProjects\\\\" \
                                        "sqlAlchemy\\\\sqlAlchemy\\\\models\\\\test.db"

app.app_context().push()
db.init_app(app)
db.create_all()
api.init_app(app)


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, 400


if __name__ == "__main__":
    app.run(debug=True)