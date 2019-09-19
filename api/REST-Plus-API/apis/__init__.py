from flask_restplus import Api
from apis.aws_ops import namespace as awsnamespace
from apis.todos import todonamespace
from apis.movies import namespace as moviesnamespace

api = Api(
    title='Learn-API',
    version='V1',
    description='Learning API'
)

api.add_namespace(awsnamespace)
api.add_namespace(todonamespace)
api.add_namespace(moviesnamespace, path="/v1/movies")
