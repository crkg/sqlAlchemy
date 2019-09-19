import sys
sys.path.append("c:\\Users\\ramesh.kg\\PycharmProjects\\AWS")
from flask import Flask
from AWS.apis import api


app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)




