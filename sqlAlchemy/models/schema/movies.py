from sqlAlchemy.models.utils.base_db import db

class Movies(db.Model):
    movie_name = db.Column(db.String(90), primary_key=True)
    year = db.Column(db.Integer)
    director = db.Column(db.String(80))

    def __init__(self, dict_args):
        self.director = dict_args.get('director')
        self.movie_name = dict_args.get('movie_name')
        self.year = int(dict_args.get('year'))

    def to_obj(self):
        return {
            "movie_name": self.movie_name,
            "year": self.year,
            "director": self.director
        }
