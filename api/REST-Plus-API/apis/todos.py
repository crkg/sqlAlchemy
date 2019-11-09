from flask_restplus import Resource, fields, reqparse, Namespace
from flask import request

todonamespace = Namespace("TODO's", description='To play with Dictonary')

parselevel=reqparse.RequestParser()
parselevel.add_argument('todo_id', type=str, required=True)
parselevel.add_argument('todo_data', type=str, required=True)


model = todonamespace.model('postInput', {
    'todo_id': fields.String,
    'todo_data': fields.String

})

todos={}


@todonamespace.route('/todos')
class TodoSimple(Resource):
    @todonamespace.response(201, 'accepted')
    @todonamespace.response(400, 'Bad request')
    @todonamespace.response(500, 'Internal server error')
    @todonamespace.response(404, 'Not found')
    @todonamespace.response(403, 'Unauthorized')
    @todonamespace.expect(model)
    def post(self):
        payload = request.get_json()
        print(payload)
        key = payload.get('todo_id')
        value = payload.get('todo_data')
        todos[key] = value
        return {}, 201

    @todonamespace.response(200, 'success')
    @todonamespace.response(400, 'Bad request')
    @todonamespace.response(500, 'Internal server error')
    @todonamespace.response(404, 'Not found')
    @todonamespace.doc(parser=parselevel)
    @todonamespace.marshal_with(model, code=200)
    def get(self):
        payload=parselevel.parse_args()
        print(payload)
        key = payload.get('todo_id')
        value = payload.get('todo_data')
        return payload, 200
