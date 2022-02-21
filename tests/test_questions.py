"""
Tests for forms route
"""
from config.settings import settings
from server.schemas.questions import Questions
from tests.test_main import client

jwt_test = settings.test_jwt
header = f"Authorization Bearer {jwt_test}"
ROUTE = "/forms_questions/"
body = {"domain": "AMBIENCE"}
res = Questions(
    question="", is_subjective=True, options=[], year=1, domain_id=1
).serialize()
res["answers"] = ""


async def get_questions():
    """
    get questions for specified domain
    """
    post_response = client.post(ROUTE, body, headers=header)
    assert post_response.status_code == 200
    assert post_response.json() == {"questions": [res]}


async def get_questions_error():
    """
    get questions for specified domain
    """
    post_response = client.post(ROUTE, body, headers=header)
    assert post_response.status_code == 500
    assert post_response.json() == {"detail": "INTERNAL SERVER ERROR"}
