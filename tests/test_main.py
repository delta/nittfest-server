"""
Test
"""
from fastapi.testclient import TestClient

from config.database import TestSessionLocal
from server.main import app

client = TestClient(app)


def get_database():
    """
    Dependency function to get
    SessionLocal for testing
    """
    try:
        database = TestSessionLocal()
        yield database
    finally:
        database.close()
