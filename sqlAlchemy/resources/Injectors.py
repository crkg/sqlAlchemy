from sqlAlchemy.resources.movies_ops import MovieOperations
from sqlAlchemy.models.utils.movies import MovieDbOperations


def ins_creation:
    movies_ops_ins = MovieOperations()
    movies_db_ins = MovieDbOperations()
    return movies_db_ins, movies_ops_ins

