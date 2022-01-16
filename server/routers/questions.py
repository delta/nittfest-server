"""
Form Questions Model
"""
from fastapi import APIRouter, HTTPException, Depends
from server.models.questions import DomainModel, DomainResponseModel
from server.config.database import SessionLocal
from server.schemas.questions import Questions
from server.controllers.auth import JWTBearer
from server.config.logger import logger

router = APIRouter(
    prefix="/form_questions",
)


@router.post(
    "/",
    response_model=DomainResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def form_questions(domain: DomainModel) -> DomainResponseModel:
    """
    POST route for form questions
    """
    try:
        database = SessionLocal()
        if domain.domain == "PRC":
            questions = (
                database.query(Questions).filter_by(domain="PRC").all()
            )
        elif domain.domain == "NOC":
            questions = (
                database.query(Questions).filter_by(domain="NOC").all()
            )
        elif domain.domain == "MARKETING":
            questions = (
                database.query(Questions)
                .filter_by(domain="MARKETING")
                .all()
            )
        elif domain.domain == "ALL":
            questions = database.query(Questions).all()
        else:
            questions = []
        database.close()
        logger.info(f"{domain.domain} form questions retrieved")
        return {"questions": questions}
    except Exception as exception:
        logger.error(
            f"{domain.domain} form questions retrieval failed due to {exception}"
        )
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred.",
            headers={"X-Error": str(exception)},
        ) from exception
