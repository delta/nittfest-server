"""
Seed Question data
"""

from scripts.constants import domains
from config.database import SessionLocal
from config.logger import logger
from server.schemas.domains import Domains


async def seed_domains():
    """
    Seed the database with teams
    """
    try:
        database = SessionLocal()
        if database.query(Domains).count() == 0:
            logger.info("Seeding database with domains")
            for domain in domains:
                database.add(
                    Domains(
                        domain=domain["domain"],
                        description=domain["description"],
                    )
                )
            database.commit()
            logger.info("Successfully seeded database with domains")
            database.close()
    except Exception as exception:
        logger.error(f"failed to seed domains {exception}")
        database.rollback()
        database.close()
        raise exception
