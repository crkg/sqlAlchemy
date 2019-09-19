import os
import sys
sys.path.append("/Users/ramesh/PycharmProjects/sqlAlchemy")
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from sqlAlchemy.app_file import app, db


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def routes():
    '''show all routes available'''
    print(app.url_map)


@manager.command
def run():
    '''Run app'''
    routes()
    app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)


@manager.command
def rm_pyc():
    '''Remove all pyc on bash only'''
    os.system('find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete')

if __name__ == '__main__':
    manager.run()
