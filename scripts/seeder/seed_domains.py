"""
Seed Question data
"""

from sqlalchemy.orm import Session

from config.logger import logger
from scripts.constants import domains
from server.schemas.domains import Domains


async def seed_domains(database: Session):
    """
    Seed the database with teams
    """
    try:
        if database.query(Domains).count() == 0:
            logger.info("Seeding database with domains")
            for domain in domains:
                database.add(
                    Domains(
                        domain=domain["domain"],
                        description=domain["description"],
                    )
                )
            logger.info("Successfully seeded database with domains")
        database.commit()
        database.close()
    except Exception as exception:
        logger.error(f"failed to seed domains {exception}")
        database.rollback()
        database.close()
        raise exception
