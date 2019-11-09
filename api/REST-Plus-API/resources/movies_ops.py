import os

class MovieOperations:

    def getallmovies(self):
        fpath = os.path.abspath("resources\movies.csv")
        print(fpath)
        if not fpath or not os.path.exists(fpath):
            raise Exception("file not found")
        with open(fpath, 'r') as fopen:
            data = fopen.readlines()
        return data

    def getmoviesbydir(self, director):
        result = self.getallmovies()
        print(result)
        if result:
            moviedata=[each_item.rstrip().split(',')[0] for each_item in result
                       if each_item.rstrip().split(',')[2].upper() == director.upper()]
            return moviedata
        else:
            raise Exception("movies not found")


if __name__ == '__main__':
    movie = MovieOperations()
    print(movie.getmoviesbydir('FrancisLawrence'))
