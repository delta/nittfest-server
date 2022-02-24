"""
Test
"""

from fastapi.testclient import TestClient

from config.database import (
    Base,
    TestingSessionLocal,
    get_database,
    get_test_database,
    test_engine,
)
from scripts.seeder.seed_tests import seed_testdb
from server.main import app

Base.metadata.create_all(bind=test_engine)


async def test():
    """
    seed tests
    """
    await seed_testdb(database=TestingSessionLocal())
    return TestClient(app)


app.dependency_overrides[get_database] = get_test_database
client = test()
