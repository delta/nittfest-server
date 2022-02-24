"""
Main File
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import Base, engine
from config.settings import settings
from server.routers import admin, auth, preferences, questions, seeds

app = FastAPI()
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(preferences.router)
app.include_router(seeds.router)
app.include_router(admin.router)

origins = [settings.frontend_url]

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
