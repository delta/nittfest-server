"""
seeding route
"""
from fastapi import APIRouter

from scripts.seeder.seed_domains import seed_domains
from scripts.seeder.seed_questions import seed_questions
from scripts.seeder.seed_tests import seed_testdb

router = APIRouter()


@router.on_event("startup")
async def seed():
    """
    Seeds Domain when server starts
    """
    await seed_domains()
    await seed_questions()
    await seed_testdb()
