"""
Database Config
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import (
    declarative_base,
)
from sqlalchemy.orm import sessionmaker
from server.config.settings import settings

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
