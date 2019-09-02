from sqlAlchemy.models.utils.base_db import db
from sqlAlchemy.models.schema.movies import Movies
from sqlalchemy import text

class MovieDbOperations:

    @staticmethod
    def create(dict_args):
        try:
            print(dict_args)
            movies_model_ins = Movies(dict_args)
            db.session.add(movies_model_ins)
            db.session.commit()
        except Exception as Error:
            print(Error)
            db.session.rollback()
            raise Exception(Error)
        finally:
            db.session.close()

    @staticmethod
    def delete(moviename):
        try:
            db.session.query(Movies).filter(text(f"movies.movie_name={moviename}")).delete(synchronize_session=False)
            db.session.commit()
        except Exception as Error:
            db.session.rollback()
            raise Exception(Error)
        finally:
            db.session.close()

    @staticmethod
    def update(dict_args):
        try:
            db.session.query(Movies).filter(text(f"movies.movie_name={moviename}")).update(dict_args,
                                                                                           synchronize_session=False)
            db.session.commit()
        except Exception as Error:
            db.session.rollback()
            raise Exception(Error)
        finally:
            db.session.close()

    def select(self, condition, all_row):
        try:
            if all_row:
                return self._select_all(condition)
            else:
                return self._select_one(condition)
        except Exception as Error:
            db.session.rollback()
            raise Exception(Error)
        finally:
            db.session.close()


    def _select_one(self,condition):
        if condition:
            result = db.session.query(Movies).filter(text(condition)).first()
        else:
            result = db.session.query(Movies).first()
        if result:
            return [result.to_obj()]
        else:
            return []

    def _select_all(self, condition):
        if condition:
            result = db.session.query(Movies).filter(text(condition)).all()
        else:
            result = db.session.query(Movies).all()
        if result:
            return [each_row.to_obj() for each_row in result if each_row]
        else:
            return []
