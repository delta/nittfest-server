"""
Tests for department route
"""
from fastapi.testclient import TestClient

ROUTE = "/department"
res = {
    "departments": [
        {"name": "MME", "description": "Gods"},
        {"name": "EEE", "description": "some generic description"},
        {"name": "ICE", "description": "some generic description"},
    ]
}


def get_departments(client: TestClient):
    """
    get list of department
    """
    get_response = client.get(url=ROUTE)
    assert get_response.status_code == 200
    assert get_response.json() == res
