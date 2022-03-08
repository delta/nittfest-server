"""
Tests for department route
"""
from fastapi.testclient import TestClient

ROUTE = "/department"
res = {
    "departments": [
        {
            "name": "cse",
            "description": "cse",
        },
        {
            "name": "archi",
            "description": "archi",
        },
        {
            "name": "eee",
            "description": "eee",
        },
    ]
}


def get_departments(client: TestClient):
    """
    get list of department
    """
    get_response = client.get(url=ROUTE)
    assert get_response.status_code == 200
    assert get_response.json() == res
