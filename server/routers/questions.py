"""
Form Questions Model
"""
from fastapi import APIRouter, HTTPException, Depends
from server.models.questions import (
    AnswerRequestModel,
    AnswerResponseModel,
    QuestionRequestModel,
    QuestionResponseModel,
)
from server.models.errors import GenericError
from server.config.database import SessionLocal
from server.schemas.questions import Questions, Answer
from server.schemas.users import Users
from server.controllers.auth import JWTBearer, decode_jwt
from server.config.logger import logger

router = APIRouter(
    prefix="/form_questions",
)


@router.post(
    "/",
    response_model=QuestionResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def form_questions(
    domain: QuestionRequestModel,
) -> QuestionResponseModel:
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


@router.post(
    "/submit",
    response_model=AnswerResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def form_questions_submit(
    answers: AnswerRequestModel,
    token: str = Depends(JWTBearer()),
) -> AnswerResponseModel:
    """
    POST route for form questions
    """
    try:
        database = SessionLocal()
        email = decode_jwt(token)["user_email"]
        user = database.query(Users).filter_by(email=email).first()
        if not user:
            database.close()
            raise GenericError("User not found")
        for answer in answers.answers:
            # If user_id and question_id are not found, then create a new answer
            if (
                not database.query(Answer)
                .filter_by(
                    user_id=user.id, question_id=answer["question_id"]
                )
                .first()
            ):
                database.add(
                    Answer(
                        user_id=user.id,
                        question_id=answer["question_id"],
                        answer=answer["answer"],
                    )
                )
            else:
                # If user_id and question_id are found, then update the answer
                database.query(Answer).filter_by(
                    user_id=user.id, question_id=answer["question_id"]
                ).update({"answer": answer["answer"]})

        database.commit()
        database.close()
        logger.info(f"{email} form answers submitted")
        return {"message": "Answers submitted successfully"}

    except GenericError as exception:
        logger.error(
            f"{email} form answers submission failed due to {exception}"
        )
        raise HTTPException(
            status_code=403,
            detail="User not found",
        ) from exception

    except Exception as exception:
        logger.error(
            f"{email} form questions submission failed due to {exception}"
        )
        raise HTTPException(
            status_code=500,
            detail="Form answers submission failed.",
            headers={"X-Error": str(exception)},
        ) from exception
