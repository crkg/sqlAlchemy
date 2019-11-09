from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

model = api.model('postInput', {
    'todo_id': fields.String,
    'todo_data': fields.String

})

awsschema = api.model('AWS', {
    'region': fields.String(description='Select the aws region', required=True),
    'State': fields.String(description='Select the aws server state', required=True)
})

parselevel=reqparse.RequestParser()
parselevel.add_argument('todo_id', type=str, required=True)
parselevel.add_argument('todo_data', type=str, required=True)



awsparselevel = reqparse.RequestParser()
awsparselevel.add_argument('region', choices=('AsiaSpecific', 'US-East'), help='Bad choice select one of the regions')
awsparselevel.add_argument('State', choices=('ON', 'OFF'))


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, 400

@api.route('/<string:todo_id>')
@api.doc(params={'todo_id': 'key name of the dic'},description="To play with dictonaries")

class TodoSimple(Resource):

    @api.response(200,'success')
    @api.response(400, 'Bad request')
    @api.response(500, 'Internal server error')
    @api.response(404, 'Not found')
    @api.response(403, 'Unauthorized')
    @api.doc(description="\n To get the values of the key")
    def get(self, todo_id):
        """ checking the value"""
        if todos:

            if todos.get(todo_id):
                return {todo_id: todos.get(todo_id)}, 200
            else:
                return {todo_id: f"{todo_id} is not found"}, 404
        else:
                raise Exception("dictionary not found")

    def put(self, todo_id):
        print(todo_id)
        todos[todo_id] = todo_id
        return {todo_id: todos[todo_id]}


@api.route('/todos')
class TodoSimple(Resource):
    @api.response(201, 'accepted')
    @api.response(400, 'Bad request')
    @api.response(500, 'Internal server error')
    @api.response(404, 'Not found')
    @api.response(403, 'Unauthorized')
    @api.expect(model)
    def post(self):
        payload = request.get_json()
        print(payload)
        key = payload.get('todo_id')
        value = payload.get('todo_data')
        todos[key] = value
        return {}, 201

    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    @api.response(500, 'Internal server error')
    @api.response(404, 'Not found')
    @api.doc(parser=parselevel)
    @api.marshal_with(model, code=200)
    def get(self):
        payload=parselevel.parse_args()
        print(payload)
        key = payload.get('todo_id')
        value = payload.get('todo_data')
        return payload, 200


@api.route('/aws-state')
class TodoSimple(Resource):
    @api.response(200,'success')
    @api.response(400, 'Bad request')
    @api.response(500, 'Internal server error')
    @api.response(404, 'Not found')
    @api.response(403, 'Unauthorized')
    @api.expect(awsschema, validate=True)
    def post(self):
        try:
            data = self.parsing_args()
            region = data.get('region')
            state = data.get('State')
            return {'region': region, 'state': state}
        except Exception as exc:
                return {'error': str(exc)}, 500

    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    @api.response(500, 'Internal server error')
    @api.response(404, 'Not found')
    @api.response(403, 'Unauthorized')
    @api.doc(parser=awsparselevel)
    def get(self):
        awsattr=awsparselevel.parse_args()
        return awsattr


    @staticmethod
    def parsing_args():
        parselevel = reqparse.RequestParser()
        parselevel.add_argument('region', help='Bad choice select one of the regions')
        parselevel.add_argument('State')
        return parselevel.parse_args()



if __name__ == '__main__':
    app.run(debug=True)