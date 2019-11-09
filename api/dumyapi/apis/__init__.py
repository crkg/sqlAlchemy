from flask_restplus import Api
from dumyapi.apis.language_api import langnamespace


authorization = {
    'Basic Auth': {'type': 'basic',
                   'in': 'header',
                   'name': 'authorization'
                   }
}

api = Api(
    title='Language-API',
    version='V1',
    description='Lunguage API',
    security='Basic Auth',
    authorizations=authorization
)

api.add_namespace(langnamespace, path="/v1")


