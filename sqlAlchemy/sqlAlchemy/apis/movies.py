from flask_restplus import Resource, fields, reqparse, Namespace
from sqlAlchemy.resources.movies_ops import MovieOperations

parselevel=reqparse.RequestParser()
parselevel.add_argument('directorname', type=str, required=True, help='Enter the director name')

namespace = Namespace('Movies', description='to movies from file')

movieschema = namespace.model('Movies', {
    'Director': fields.String(description='Director name', required=True),
    'Movie Name': fields.String(description='Movie name', required=True),
    'Release Year': fields.Integer(description='Year of release', required=True)
})

@namespace.route('/movies')
class TodoSimple(Resource):
    @namespace.response(200, 'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    # @namespace.doc(parser=awsparselevel)
    def get(self):

        mov_ins = MovieOperations()
        result = mov_ins.getallmovies()
        if not result:
            return {"movies": "movies not found"}, 404
        else:
            return {"movies": result}, 200

    @namespace.response(201, 'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    @namespace.expect(movieschema)
    def post(self):
        payload = self.parsing_args()
        print(payload)
        insert_db = MovieOperations().insertintodb(payload)
        if insert_db == 'success':
            return 'success', 201

    @staticmethod
    def parsing_args():
        parselevel = reqparse.RequestParser()
        parselevel.add_argument('Director', type=str, required=True)
        parselevel.add_argument('Movie Name', type=str, required=True)
        parselevel.add_argument('Release Year', type=int, required=True)
        return parselevel.parse_args()


@namespace.route('/directorname')
class TodoSimpleDirector(Resource):
    @namespace.response(200, 'success')
    @namespace.response(400, 'Bad request')
    @namespace.response(500, 'Internal server error')
    @namespace.response(404, 'Not found')
    @namespace.response(403, 'Unauthorized')
    @namespace.doc(parser=parselevel)
    def get(self):
        payload = parselevel.parse_args()
        print(payload)
        directorname = payload.get('directorname')
        mov_ins = MovieOperations()
        result = mov_ins.getmoviesbydir(directorname)
        if not result:
            return {"movies": "movies not found"}, 404
        else:
            return {"movies": result}, 200


