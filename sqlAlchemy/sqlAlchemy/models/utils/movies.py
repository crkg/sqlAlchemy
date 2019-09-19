from sqlAlchemy.models.utils.base_db import db
from sqlAlchemy.models.utils.database_session import Persistance
from sqlAlchemy.models.schema.movies import Movies
from sqlalchemy import text


class MovieDbOperations:

    @staticmethod
    def create(dict_args):
            #print(dict_args)
            movies_model_ins = Movies(dict_args)
            with Persistance().session as session:
                session.add(movies_model_ins)

    @staticmethod
    def delete(moviename):
        with Persistance().session as session:
            session.query(Movies).filter(text(f"movies.movie_name={moviename}")).delete(synchronize_session=False)

        #try:
        #    db.session.query(Movies).filter(text(f"movies.movie_name={moviename}")).delete(synchronize_session=False)
        #    db.session.commit()
        #except Exception as Error:
        #    db.session.rollback()
        #    raise Exception(Error)
        #finally:
        #    db.session.close()

    @staticmethod
    def update(dict_args):
        with Persistance().session as session:
            session.query(Movies).filter(text(f"movies.movie_name={dict_args.get('moviename')}")).update(dict_args,
                                                                                           synchronize_session=False)
    #    try:
    #        db.session.query(Movies).filter(text(f"movies.movie_name={moviename}")).update(dict_args,
    #                                                                                       synchronize_session=False)
    #        db.session.commit()
    #    except Exception as Error:
    #        db.session.rollback()
    #        raise Exception(Error)
    #    finally:
    #        db.session.close()

    def select(self, condition, all_row):
        if all_row:
            return self._select_all(condition)
        else:
            return self._select_one(condition)

    def _select_one(self,condition):
        with Persistance().session as session:
            if condition:
                result = session.query(Movies).filter(text(condition)).first()
            else:
                result = session.query(Movies).first()
        if result:
            return [result.to_obj()]
        else:
            return []

    def _select_all(self, condition):
        with Persistance().session as session:
            if condition:
                result = session.query(Movies).filter(text(condition)).all()
            else:
                result = session.query(Movies).all()
        if result:
            return [each_row.to_obj() for each_row in result if each_row]
        else:
            return []
