from flask_restplus import Resource, fields, reqparse, Namespace

namespace = Namespace('AWS', description='to work aws')

awsschema = namespace.model('AWS', {
    'region': fields.String(description='Select the aws region', required=True),
    'State': fields.String(description='Select the aws server state', required=True)
})

awsparselevel = reqparse.RequestParser()
awsparselevel.add_argument('region', choices=('AsiaSpecific', 'US-East'), help='Bad choice select one of the regions')
awsparselevel.add_argument('State', choices=('ON', 'OFF'))



@namespace.route('/aws-state')
class TodoSimple(Resource):
    @namespace.response(200,'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    @namespace.expect(awsschema, validate=True)
    def post(self):
        try:
            data = self.parsing_args()
            region = data.get('region')
            state = data.get('State')
            return {'region': region, 'state': state}
        except Exception as exc:
                return {'error': str(exc)}, 500

    @namespace.response(200, 'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    @namespace.doc(parser=awsparselevel)
    def get(self):
        awsattr=awsparselevel.parse_args()
        return awsattr


    @staticmethod
    def parsing_args():
        parselevel = reqparse.RequestParser()
        parselevel.add_argument('region', help='Bad choice select one of the regions')
        parselevel.add_argument('State')
        return parselevel.parse_args()