"""
Tests for preferences route
"""
from config.settings import settings
from tests.test_main import client

jwt_test=settings.test_jwt
header = f"Authorization Bearer {jwt_test}"
ROUTE = "/preferences/"

body={
    "email": "string",
    "preferences": [
        "EVENTS",
        "AMBIENCE",
        "MARKETING"
    ]
    }

async def check_preferences_first_fill():
    """
    post prefs for first time and check prefs
    """
    post_response = client.post(ROUTE ,body,headers=header)
    assert post_response.status_code==200
    assert post_response.json() == {"status": True}
    get_response = client.get(ROUTE , headers=header)
    assert get_response.status_code == 200
    assert get_response.json() == {"status":True}

async def check_preferences_already_filled():
    """
    post prefs another time and check prefs
    """
    post_response = client.post(ROUTE ,body,headers=header)
    assert post_response.status_code==403
    assert post_response.json() == {"detail": "Preferences Already Filled"}
    get_response = client.get(ROUTE , headers=header)
    assert get_response.status_code == 200
    assert get_response.json() == {"status":True}
