"""
Database Config
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import settings

engines = {
    'main':create_engine(settings.sqlalchemy_database_url),
    'test':create_engine(settings.sqlalchemy_database_test_url)
}
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engines['main'])

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engines['test'])

Base = declarative_base()
