"""
Nerdle Route
"""
import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.controllers.auth import JWTBearer, decode_jwt
from server.models.errors import GenericError
from server.models.nerdle import (
    WinningGuessModel,
    WordResponseModel,
    GuessesResponseModel,
    GuessValidationRequestModel,
    GuessValidationResponseModel,
)
from server.schemas.guesses import Guesses
from server.schemas.nerdle import Nerdle
from server.schemas.users import Users
from server.controllers.nerdle import validate_guess_controller

router = APIRouter(
    prefix="/nerdle",
)

word_list = ["panda", "cycle"]


@router.post(
    "/set_word",
    response_model=WordResponseModel,
    dependencies=[Depends(JWTBearer), Depends(get_database)],
)
async def get_word(
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> WordResponseModel:
    """
    GET route for setting a word
    """
    try:
        user_email = decode_jwt(token)["user_email"]
        user_id = (
            database.query(Users.id)
            .filter(Users.email == user_email)
            .first()
        )
        if user_id is None:
            raise GenericError("User not found")
        nerdle = (
            database.query(Nerdle)
            .filter(Nerdle.user_id == user_id)
            .first()
        )
        guesses = (
            database.query(Guesses)
            .filter(Guesses.user_id == user_id)
            .all()
        )
        if len(guesses) > 0:
            raise GenericError("Cannot change word mid guessing")
        if nerdle is None:
            nerdle = Nerdle(
                user_id=user_id,
                current_word="",
                score=0,
                streak=0,
            )
        if nerdle.current_word == "":
            generated_word = word_list[
                random.randint(0, len(word_list) - 1)
            ]
            nerdle.current_word = generated_word
        database.add(nerdle)
        database.commit()
        return WordResponseModel(status="Successful")
    except Exception as exception:
        logger.error("Error in get_word: " + str(exception))
        raise HTTPException(
            status_code=500,
            detail="Form answers submission failed.",
            headers={"X-Error": "Error in getting word"},
        ) from exception


@router.get(
    "/get_guesses",
    response_model=GuessesResponseModel,
    dependencies=[Depends(JWTBearer), Depends(get_database)],
)
async def get_guesses(
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> GuessesResponseModel:
    """
    GET route for getting guesses
    """
    try:
        user_email = decode_jwt(token)["user_email"]
        user_id = (
            database.query(Users.id)
            .filter(Users.email == user_email)
            .first()
        )
        if user_id is None:
            raise GenericError("User not found")
        guesses = (
            database.query(Guesses)
            .filter(Guesses.user_id == user_id)
            .all()
            .sort(key=lambda guess: guess.position)
        )
        return GuessesResponseModel(
            guesses=guesses,
        )
    except Exception as exception:
        logger.error("Error in get_guesses: " + str(exception))
        raise HTTPException(
            status_code=500,
            detail="Form answers submission failed.",
            headers={"X-Error": "Error in getting guesses"},
        ) from exception


@router.post(
    "/validate_guess",
    response_model=GuessValidationResponseModel,
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
)
async def validate_guess(
    unvalidated_guess: GuessValidationRequestModel,
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> GuessValidationResponseModel:
    """
    Route to Validate Guess
    """
    try:
        email = decode_jwt(token)["user_email"]
        user_id = (
            database.query(Users.id).filter(Users.email == email).first()
        )
        if not user_id:
            raise GenericError("User not found")
        answer = (
            database.query(Nerdle.current_word)
            .filter(Nerdle.user_id == user_id)
            .first()
        )
        validated_guess_response: WinningGuessModel = (
            validate_guess_controller(
                answer=answer, unvalidated_guess=unvalidated_guess
            )
        )
        guesses = database.query(Guesses).all()
        guess = Guesses(
            guess=unvalidated_guess,
            user_id=user_id,
            position=len(guesses) + 1,
        )
        database.add(guess)
        database.commit()
        return GuessValidationResponseModel(
            validated_guess=validated_guess_response.validated_guess
        )
    except Exception as exception:
        logger.error("Failed to Validate Guess")
        raise HTTPException(
            status_code=500,
            detail="Guess Validation Failed",
            headers={"X-Error": "Error Validating Guess"},
        ) from exception
