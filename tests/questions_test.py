"""
Tests for forms route
"""
import json

from fastapi.testclient import TestClient

from config.settings import settings

jwt_test = settings.test_jwt
header = {"Authorization": f"Bearer {jwt_test}"}
ROUTE = "/form_questions/"
body = json.dumps({"domain": "EVENTS"})
res = {
    "questions": [
        {
            "id": 1,
            "question": "Which is best club in NITT ?",
            "is_subjective": True,
            "options": None,
            "answer": "DeltaForce",
        }
    ]
}


def get_questions(client: TestClient):
    """
    get questions for specified domain
    """
    post_response = client.post(ROUTE, data=body, headers=header)
    assert post_response.status_code == 200
    print(f"{res}  value:{post_response.json()}")
    assert post_response.json() == res


def get_questions_error(client: TestClient):
    """
    get questions for specified domain
    """
    post_response = client.post(ROUTE, data=body, headers=header)
    assert post_response.status_code == 500
    assert post_response.json() == {"detail": "INTERNAL SERVER ERROR"}
