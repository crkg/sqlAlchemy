from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlAlchemy.models.utils.base_db import db


def sql_engine(db_config: dict):
    '''This is for test case usage'''
    db_uri = (
        f"postgresql://{db_config['user']}:{db_config['password']}"
        f"@{db_config['db_host']}:{db_config['db_port']}/{db_config['database']}"
    )
    return create_engine(db_uri, convert_unicode=True)

engine=db.get_engine()
SESSION = scoped_session(sessionmaker(bind=engine, autocommit=True, expire_on_commit=False))
Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine
Base.query = SESSION.query_property()

@contextmanager
def session_scope():
    '''Provide a transactional scope around a series of operations'''
    session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
    try:
        yield session
        session.commit()
    except Exception as Error:
        session.rollback()
        raise Exception(Error)
    finally:
        session.close()


class Persistance:
    '''Handle database releated actions/attributes'''
    @property
    def engine(self):
        '''Database enginer property'''
        return engine

    @property
    def base(self):
        '''Database base propery'''
        return Base

    @property
    def session(self):
        '''Database session propery'''
        return session_scope()
