"""
Main File
"""

import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import Base, engine
from config.settings import settings
from server.routers import department, event

if "pytest" in sys.modules:
    from server.routers import auth, preferences, questions, tshirt, scores
else:
    from server.routers import (
        admin,
        auth,
        preferences,
        questions,
        seeds,
        scores,
        tshirt,
    )

app = FastAPI()

app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(preferences.router)
app.include_router(department.router)
app.include_router(event.router)
app.include_router(tshirt.router)
app.include_router(scores.router)
origins = []

if "pytest" not in sys.modules:
    app.include_router(seeds.router)
    app.include_router(admin.router)
    Base.metadata.create_all(bind=engine)
    origins.append(settings.frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
