import sys
sys.path.append("c:\\Users\\ramesh.kg\\PycharmProjects\\Flask-REST-full\\")
from flask import Flask
from apis import api


app = Flask(__name__)
api.init_app(app)


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, 400


if __name__ == "__main__":
    app.run(debug=True)

