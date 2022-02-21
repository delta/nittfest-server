"""
Seed Question data
"""

from scripts.test_constants import test_domains,test_answers,test_prefs,test_questions,test_user
from config.database import TestSessionLocal
from config.logger import logger
from server.schemas.domains import Domains
from server.schemas.users import Users
from server.schemas.preferences import Preferences
from server.schemas.questions import Questions,Answer


async def seed_testdb():
    """
    Seed the database with teams
    """
    try:
        database = TestSessionLocal()
        logger.info("Seeding test database")
        if database.query(Domains).count() == 0:
            for domain in test_domains:
                database.add(
                    Domains(
                        domain=domain["domain"],
                        description=domain["description"],
                    )
                )
        if database.query(Users).count() == 0:
            database.add(
                Users(
                   name=test_user["name"],
                   email=test_user["email"],
                   mobile_number=test_user["mobile_number"],
                   gender=test_user["gender"]
                )
            )
        if database.query(Preferences).count() == 0:
            for prefs in test_prefs:
                database.add(
                    Preferences(
                        user_id=prefs["user_id"],
                        preference_no=prefs["preference_no"],
                        domain_id=prefs["domain_id"]
                    )
                )
        if database.query(Questions).count() == 0:
            for question in test_questions:
                database.add(
                    Questions(
                        question=question["question"],
                        is_subjective=prefs["is_subjective"],
                        domain_id=prefs["domain_id"],
                        options=[],
                        year=prefs["year"],
                    )
                )
        if database.query(Answer).count() == 0:
            for answer in test_answers:
                database.add(
                    Answer(
                        answer=answer["answer"],
                        question_id=answer["question_id"],
                        user_id=answer["user_id"]
                    )
                )
        database.commit()
        logger.info("Successfully seeded test database")
        database.close()
    except Exception as exception:
        logger.error(f"failed to seed tests {exception}")
        database.rollback()
        database.close()
        raise exception
