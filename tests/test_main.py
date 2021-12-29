"""
Test
"""
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_read_main():
    """
    Mock response
    """
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
