"""
Seed Question data
"""

from sqlalchemy.orm import Session

from config.logger import logger
from scripts.constants import questions
from server.schemas.domains import Domains
from server.schemas.questions import Questions


async def seed_questions(database: Session):
    """
    Seed the database with questions
    """
    try:
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
            logger.info("Successfully seeded database with questions")
        database.commit()
        database.close()
    except Exception as exception:
        logger.error(f"failed to seed questions {exception}")
        database.rollback()
        database.close()
        raise exception
