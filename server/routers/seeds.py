"""
seeding route
"""

from fastapi import APIRouter
from sqlalchemy.orm.session import Session

from config.database import SessionLocal
from scripts.seeder.seed_details import seed_maindb

router = APIRouter()


@router.on_event("startup")
async def seed():
    """
    Seeds Domain when server starts
    """
    database: Session = SessionLocal()
    await seed_maindb(database=database)
    database.commit()
    database.close()
