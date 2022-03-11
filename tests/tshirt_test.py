"""
Tests for tshirt route
"""
import json

from fastapi.testclient import TestClient

from config.settings import settings

jwt_test = settings.test_jwt
header = {"Authorization": f"Bearer {jwt_test}"}
ROUTE = "/register_tshirt"
body = json.dumps({"size": "M"})


def tshirt_registration(client: TestClient):
    """
    get questions for specified domain
    """
    post_response = client.post(url=ROUTE, data=body, headers=header)
    assert post_response.status_code == 200
    assert post_response.json() == {
        "message": "Tshirt Registration successfull"
    }
