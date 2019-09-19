from flask_restplus import Api
from sqlAlchemy.apis.movies import namespace as moviesnamespace

api = Api(
    title='Learn-API',
    version='V1',
    description='Learning API'
)

api.add_namespace(moviesnamespace, path="/v1/movies")
