"""
Test
"""
from fastapi.testclient import TestClient

from server.main import app
from config.database import TestSessionLocal

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
