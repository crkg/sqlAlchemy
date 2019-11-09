from flask_restplus import Resource, fields, reqparse, Namespace
from resources.movies_ops import MovieOperations

parselevel=reqparse.RequestParser()
parselevel.add_argument('directorname', type=str, required=True, help='Enter the director name')

namespace = Namespace('Movies', description='to movies from file')

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


@namespace.route('/directorname')
class TodoSimple(Resource):
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
