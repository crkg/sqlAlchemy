import sys
sys.path.append("c:\\Users\\ramesh.kg\\PycharmProjects\\DumyApi")
from flask import Flask
from dumyapi.apis import api


app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)