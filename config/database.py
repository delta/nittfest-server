"""
Database Config
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from server.models.errors import GenericError
from config.settings import settings

engine = create_engine(settings.sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

test_engine = create_engine(settings.sqlalchemy_database_test_url)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)


async def get_database():
    """
    Dependency function to get
    SessionLocal
    """
    database: Session = SessionLocal()
    try:
        yield database
        database.commit()
    except GenericError:
        database.rollback()
    finally:
        database.close()


async def get_test_database():
    """
    Dependency function to get
    SessionLocal for testing
    """
    test_database = TestingSessionLocal()
    try:
        yield test_database
        test_database.commit()
    except GenericError:
        test_database.rollback()
    finally:
        test_database.close()
