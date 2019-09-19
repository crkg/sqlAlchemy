from flask_restplus import Api
from AWS.apis.aws_api_endpoint import namespace as awsnamespace

api = Api(
    title='AWS Integration',
    version='v0',
    description='Creating AWS Api along with Boto 3'
)

api.add_namespace(awsnamespace)