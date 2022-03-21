"""
Test for dashboard route
"""

from fastapi.testclient import TestClient

from config.settings import settings

jwt_test = settings.test_jwt
header = {"Authorization": f"Bearer {jwt_test}"}
ROUTE = "/dashboard/"
res = {
    "department": "EEE",
    "point": 34.0,
    "position": 2,
    "upcoming_events": [],
}


def get_dashboard(client: TestClient):
    """
    get list of dashboard
    """
    get_response = client.get(url=ROUTE, headers=header)
    assert get_response.status_code == 200
    assert get_response.json() == res
