"""
Tests for forms route
"""
from config.settings import settings
from tests.test_main import client

jwt_test = settings.test_jwt
header = f"Authorization Bearer {jwt_test}"
ROUTE = "/forms_questions/"
body = {"answers": []}


async def post_answers():
    """
    get questions for specified domain
    """
    post_response = client.post(ROUTE, body, headers=header)
    assert post_response.status_code == 200
    assert post_response.json() == {
        "message": "Answers submitted successfully"
    }
