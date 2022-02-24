"""
seeding route
"""

from fastapi import APIRouter
from sqlalchemy.orm.session import Session

from config.database import SessionLocal
from scripts.seeder.seed_domains import seed_domains
from scripts.seeder.seed_questions import seed_questions

router = APIRouter()


@router.on_event("startup")
async def seed():
    """
    Seeds Domain when server starts
    """
    database: Session = SessionLocal()
    await seed_domains(database=database)
    await seed_questions(database=database)
    database.commit()
    database.close()
