"""
Seed Question data
"""

from config.database import SessionLocal
from config.logger import logger
from scripts.constants import questions
from server.schemas.domains import Domains
from server.schemas.questions import Questions


async def seed_questions():
    """
    Seed the database with questions
    """
    try:
        database = SessionLocal()
        if database.query(Questions).count() == 0:
            logger.info("Seeding database with questions")
            for question in questions:
                database.add(
                    Questions(
                        question=question["question"],
                        is_subjective=question["is_subjective"],
                        domain_id=database.query(Domains)
                        .filter_by(domain=question["domain"])
                        .first()
                        .id,
                        options=question["options"],
                        year=question["year"],
                    )
                )
            database.commit()
            logger.info("Successfully seeded database with questions")
            database.close()
    except Exception as exception:
        logger.error(exception)
        database.rollback()
        database.close()
        raise exception
