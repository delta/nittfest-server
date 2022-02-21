"""
Form Questions Model
"""
from fastapi import APIRouter, Depends, HTTPException

from config.database import SessionLocal
from config.logger import logger
from server.controllers.auth import JWTBearer, decode_jwt
from server.models.errors import GenericError
from server.models.questions import (AnswerRequestModel, AnswerResponseModel,
                                     QuestionRequestModel,
                                     QuestionResponseModel)
from server.schemas.domains import Domains
from server.schemas.questions import Answer, Questions
from server.schemas.users import Users

router = APIRouter(
    prefix="/form_questions",
)


@router.post(
    "/",
    response_model=QuestionResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def form_questions(
    domain_requested: QuestionRequestModel,
    token: str = Depends(JWTBearer()),
) -> QuestionResponseModel:
    """
    POST route for form questions
    """
    try:
        email = decode_jwt(token)["user_email"]
        year = 2 if email[5] == "0" else 1
        database = SessionLocal()
        domain = (
            database.query(Domains)
            .filter_by(domain=domain_requested.domain)
            .first()
        )
        if not domain:
            database.close()
            raise GenericError("INVALID domain requested")
        user = database.query(Users).filter_by(email=email).first()
        questions = (
            database.query(Questions)
            .filter_by(domain_id=domain.id, year=year)
            .all()
        )
        logger.info(f"{domain.domain} form questions retrieved")
        response_questions = []
        for question in questions:
            response = question.serialize()
            if (
                database.query(Answer)
                .filter_by(user_id=user.id, question_id=question.id)
                .first()
            ):
                response["answer"] = (
                    database.query(Answer)
                    .filter_by(user_id=user.id, question_id=question.id)
                    .first()
                    .answer
                )
            else:
                response["answer"] = ""
            response_questions.append(response)
        database.close()
        return {"questions": response_questions}
    except GenericError as exception:
        logger.error(
            f"{domain_requested.domain} form questions retrieval failed due to {exception}"
        )
        raise HTTPException(
            status_code=500,
            detail="INTERNAL SERVER ERROR",
            headers={"X-Error": str(exception)},
        ) from exception


@router.post(
    "/submit",
    response_model=AnswerResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def form_questions_submit(
    answers_submitted: AnswerRequestModel,
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
        for answer in answers_submitted.answers:
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
            detail=f"{exception}",
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
