"""
Test
"""
from fastapi.testclient import TestClient

from config.database import (
    Base,
    TestingSessionLocal,
    get_database,
    get_test_database,
    test_engine,
)
from scripts.seeder.seed_tests import seed_testdb
from server.main import app
from tests.answers_test import post_answers
from tests.department_test import get_departments
from tests.event_test import get_events
from tests.scores_test import get_scores
from tests.preferences_test import (
    check_preferences_already_filled,
    post_preferences_another_fill,
)
from tests.questions_test import get_questions

Base.metadata.create_all(bind=test_engine)


def test() -> TestClient:
    """
    seed tests
    """
    seed_testdb(database=TestingSessionLocal())
    return TestClient(app)


def preferences_test():
    """
    method to execute tests on preferences route
    """
    post_preferences_another_fill(client)
    check_preferences_already_filled(client)


def questions_test():
    """
    method to execute tests on questions route
    """
    get_questions(client)


def answers_test():
    """
    method to execute tests on answers route
    """
    post_answers(client)


def events_test():
    """
    method to execute tests on events route
    """
    get_events(client)


def departments_test():
    """
    method to execute tests on departments route
    """
    get_departments(client)


def scores_test():
    """
    method to execute tests on scores route
    """
    get_scores(client)


app.dependency_overrides[get_database] = get_test_database

client = test()

preferences_test()
questions_test()
answers_test()
departments_test()
events_test()
scores_test()
