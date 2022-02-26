"""
Tests for forms route
"""
import json

from fastapi.testclient import TestClient

from config.settings import settings

jwt_test = settings.test_jwt
header = {"Authorization": f"Bearer {jwt_test}"}
ROUTE = "/form_questions/submit"
body = json.dumps(
    {"answers": [{"answer": "DeltaForce", "question_id": 1}]}
)


def post_answers(client: TestClient):
    """
    get questions for specified domain
    """
    post_response = client.post(url=ROUTE, data=body, headers=header)
    assert post_response.status_code == 200
    assert post_response.json() == {
        "message": "Answers submitted successfully"
    }
