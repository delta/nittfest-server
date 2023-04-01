"""
Seed Question data
"""

from requests.sessions import Session

from config.logger import logger
from scripts.test_constants import (
    test_answers,
    test_clusters,
    test_departments,
    test_domains,
    test_events,
    test_points,
    test_prefs,
    test_questions,
    test_user,
)
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.domains import Domains
from server.schemas.event import Event
from server.schemas.point import Point
from server.schemas.preferences import Preferences
from server.schemas.questions import Answer, Questions
from server.schemas.users import Users


def seed_testdb(database: Session):
    """
    Seed the database with teams
    """
    try:
        logger.info("Seeding test database")
        if database.query(Department).count() == 0:
            for department in test_departments:
                database.add(
                    Department(
                        key=department["id"],
                        name=department["name"],
                        description=department["description"],
                    )
                )
        if database.query(Users).count() == 0:
            database.add(
                Users(
                    name=test_user["name"],
                    email=test_user["email"],
                    mobile_number=test_user["mobile_number"],
                    gender=test_user["gender"],
                    department_id=test_user["department_id"],
                    fcm_token=test_user["fcm_token"],
                )
            )
        seed_inductions_testdb(database=database)
        if database.query(Cluster).count() == 0:
            for cluster in test_clusters:
                database.add(
                    Cluster(
                        key=cluster["id"],
                        name=cluster["name"],
                        image_link=cluster["image_link"],
                    )
                )
        if database.query(Event).count() == 0:
            for event in test_events:
                database.add(
                    Event(
                        key=event["id"],
                        name=event["name"],
                        description=event["description"],
                        rules=event["rules"],
                        format=event["format"],
                        resources=event["resources"],
                        cluster_id=event["cluster_id"],
                        image_link=event["image_link"],
                        form_link=event["form_link"],
                        event_link=event["event_link"],
                        start_time=event["start_time"],
                        end_time=event["end_time"],
                        is_reg_completed=event["is_reg_completed"],
                        is_event_completed=event["is_event_completed"],
                    )
                )
        if database.query(Point).count() == 0:
            for point in test_points:
                database.add(
                    Point(
                        point=point["point"],
                        position=point["position"],
                        event_id=point["event_id"],
                        department_id=point["department_id"],
                    )
                )
        logger.info("Successfully seeded test database")
        database.commit()
        database.close()
    except Exception as exception:
        logger.error(f"failed to seed tests {exception}")
        database.rollback()
        database.close()
        raise exception


def seed_inductions_testdb(database: Session):
    """
    inductions testdb
    """
    if database.query(Domains).count() == 0:
        for domain in test_domains:
            database.add(
                Domains(
                    domain=domain["domain"],
                    description=domain["descriptions"],
                )
            )
    if database.query(Preferences).count() == 0:
        for prefs in test_prefs:
            database.add(
                Preferences(
                    user_id=prefs["user_id"],
                    preference_no=prefs["preference_no"],
                    domain_id=prefs["domain_id"],
                )
            )
    if database.query(Questions).count() == 0:
        for question in test_questions:
            database.add(
                Questions(
                    question=question["question"],
                    is_subjective=question["is_subjective"],
                    domain_id=question["domain_id"],
                    options=question["options"],
                    year=question["year"],
                )
            )
    if database.query(Answer).count() == 0:
        for answer in test_answers:
            database.add(
                Answer(
                    answer=answer["answer"],
                    question_id=answer["question_id"],
                    user_id=answer["user_id"],
                )
            )
