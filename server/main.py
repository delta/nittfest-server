"""
Main File
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth


# from sqlalchemy.orm import Session


# from .controllers import user_controller as controller
# from .schemas.user_schema import User, UserCreate
# from .config.database import SessionLocal, engine, Base

# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

origins = [
    "http://localhost:41633",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status():
    """
    get route for status
    """
    return {"status": "ok"}


# @app.post("/api/oauth/token")
# async def tokenResponse(response: Res)
# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/users/", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = controller.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return controller.create_user(db=db, user=user)
