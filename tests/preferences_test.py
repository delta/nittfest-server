"""
Tests for preferences route
"""
import json

from fastapi.testclient import TestClient

from config.settings import settings

jwt_test = settings.test_jwt
header = {"Authorization": f"Bearer {jwt_test}"}
ROUTE = "/preferences/"

body = json.dumps(
    {
        "email": "string",
        "preferences": ["EVENTS", "AMBIENCE", "MARKETING"],
    }
)


def post_preferences_first_fill(client: TestClient):
    """
    post prefs for first time and check prefs
    """
    post_response = client.post(url=ROUTE, data=body, headers=header)
    assert post_response.status_code == 200
    assert post_response.json() == {"status": True}


def post_preferences_another_fill(client: TestClient):
    """
    post prefs for another time and check prefs
    """
    post_response = client.post(url=ROUTE, data=body, headers=header)
    assert post_response.status_code == 403
    assert post_response.json() == {"detail": "Preferences Already Filled"}


def check_preferences_already_filled(client: TestClient):
    """
    check prefs
    """
    get_response = client.get(url=ROUTE, headers=header)
    assert get_response.status_code == 200
    assert get_response.json() == {"status": True}
