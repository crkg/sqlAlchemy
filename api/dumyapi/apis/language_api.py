from flask_restplus import Resource, fields, reqparse, Namespace
from flask import request
from dumyapi.core.auth import authorize

langnamespace = Namespace("Languages", description='Get languages for given user')

parselevel = reqparse.RequestParser()
parselevel.add_argument('Username', type=str, required=True)
#parselevel.add_argument('Languages', type=list, required=True)


model = langnamespace.model('postInput', {
    'username': fields.String,
    'Languages': fields.List(fields.String)
})

lang = {}

@langnamespace.route('/languages')
class language(Resource):
    @langnamespace.response(201, 'accepted')
    @langnamespace.response(400, 'Bad request')
    @langnamespace.response(500, 'Internal server error')
    @langnamespace.response(404, 'Not found')
    @langnamespace.response(403, 'Unauthorized')
    @langnamespace.expect(model)
    @authorize
    def post(self):

        '''Something'''
        payload = request.get_json()
        #print(payload)
        key = payload.get('username')
        value = payload.get('Languages')
        lang[key] = value
        return lang, 201

    @langnamespace.response(200, 'success')
    @langnamespace.response(400, 'Bad request')
    @langnamespace.response(500, 'Internal server error')
    @langnamespace.response(404, 'Not found')
    #@langnamespace.doc(parser=parselevel)
    #@langnamespace.marshal_with(model, code=200)
    @authorize
    def get(self):
        '''something2'''
        #payload=parselevel.parse_args()
        #print(payload)
        #key = payload.get('username')
        #value = payload.get('Languages')
        return lang, 200

@langnamespace.route('/languages/<username>')
class languageByUsername(Resource):
    @langnamespace.response(201, 'accepted')
    @langnamespace.response(400, 'Bad request')
    @langnamespace.response(500, 'Internal server error')
    @langnamespace.response(404, 'Not found')
    @langnamespace.response(403, 'Unauthorized')
    # @langnamespace.doc(parser=parselevel)
    @authorize
    def get(self, username):
        '''SOmething 3'''
        # payload = parselevel.parse_args()
        # key = payload.get('username')
        #value = payload.get('Languages')
        #lang[key] = value
        return lang[username], 200



