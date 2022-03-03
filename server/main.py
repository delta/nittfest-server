"""
Main File
"""

import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import Base, engine
from config.settings import settings

if "pytest" in sys.modules:
    from server.routers import auth, preferences, questions
else:
    from server.routers import (
        admin,
        auth,
        preferences,
        questions,
        seeds,
        payments,
    )

app = FastAPI()

app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(preferences.router)
origins = []

if "pytest" not in sys.modules:
    app.include_router(seeds.router)
    app.include_router(admin.router)
    app.include_router(payments.router)
    Base.metadata.create_all(bind=engine)
    origins.append(settings.frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
