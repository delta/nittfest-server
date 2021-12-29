"""
Main File
"""


from fastapi import FastAPI

# from sqlalchemy.orm import Session
from server.config.logger import logger

# from .controllers import user_controller as controller
# from .schemas.user_schema import User, UserCreate
# from .config.database import SessionLocal, engine, Base

# Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/status")
def status():
    """
    get route for status
    """
    logger.debug("FFFFdd")
    logger.info("FFFFddas")
    return {"status": "ok"}


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
