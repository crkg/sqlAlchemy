import os
from sqlAlchemy.models.utils.movies import Dboperations

class MovieOperations:

    def getallmovies(self, movies_ins: Dboperations):
        #  fpath = os.path.abspath("resources\movies.csv")
        all_db_rows = movies_ins.select(condition=None, all_row=True)
        if all_db_rows:
            return all_db_rows
        else:
            return []

    def getmoviesbydir(self, director, movie_ops_instance: Dboperations):
        condition = f"movies.director = '{director}'"
        list_by_condition = movie_ops_instance.select(condition=condition,all_row=True)
        if list_by_condition:
            return list_by_condition
        else:
            return []

    def insertintodb(self, payload, movie_ops_instance: Dboperations ):
        dict_args = {
            'director': payload.get('Director'),
            'movie_name': payload.get('Movie Name'),
            'year': payload.get('Release Year')
            }
        movie_ops_instance.create(dict_args)
        return 'success'

if __name__ == '__main__':
    movie = MovieOperations()
    #print(movie.getmoviesbydir('FrancisLawrence'))
