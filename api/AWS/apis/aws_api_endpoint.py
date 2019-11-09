from flask_restplus import Resource, fields, reqparse, Namespace
from AWS.resources.aws import AWSlistInstance

namespace = Namespace('AWS', description='Try all AWS functions')

awsschema = namespace.model('AWS', {
    'AwsRegion': fields.String(description='Select the aws region', required=True),
    'State': fields.String(description='Select the aws server state', required=True),
    'Ec2Instance': fields.String(description='Select the aws server state', required=True),
})

parselevel=reqparse.RequestParser()
parselevel.add_argument('Instance Name', type=str, required=True)
parselevel.add_argument('AWS Region', type=str, required=True)


@namespace.route('/aws-state')
#End point resource , inherting the resource to the stop instance
class GetInstanceState(Resource):
    @namespace.response(200, 'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    @namespace.doc(parser=parselevel)
    @namespace.doc(description="\n To get the status of the Instance")
    def get(self):
        awsinfo = parselevel.parse_args()
        awsregion = awsinfo.get("AWS Region")
        awsinstace = awsinfo.get("Instance Name")
        instance = AWSlistInstance()
        instancedetails = instance.listAInstance(awsregion, awsinstace)
        if instancedetails is None:
            return {'error': 'No Instance Found with the name'}, 404
        else:
            return {'Instance': instancedetails}, 200





