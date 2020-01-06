from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from .meta import Base

import configparser

config = configparser.ConfigParser()

if not config.read('GraphQL.ini'):
    raise config.Error('Could not open %s' % config)

SQLALCHEMY_DATABASE_URL = config.get('app:main','sqlalchemy.url')
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
Base.bind = engine
Base.query = SessionLocal.query_property()




