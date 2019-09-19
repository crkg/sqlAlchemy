import sys
import os
sys.path.append("/Users/ramesh/PycharmProjects/sqlAlchemy")
from flask import Flask

from sqlAlchemy.models.utils.base_db import db

def load_conf(app):
    app.config.from_object('config.app_conf_local')
    if 'CONFFILE_PATH' in os.environ:
        app.config.from_envvar('CONFFILE_PATH')

app = Flask(__name__)
load_conf(app)
app.app_context().push()
db.init_app(app)
db.create_all()
from sqlAlchemy.apis import api
api.init_app(app)


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, 400


if __name__ == "__main__":
    app.run(debug=True)
