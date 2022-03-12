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
    NerdleScoreResponseModel,
)
from server.schemas.guesses import Guesses
from server.schemas.nerdle import Nerdle
from server.schemas.users import Users
from server.controllers.nerdle import (
    validate_guess_controller,
    is_valid_word,
)
from scripts.constants import word_list

router = APIRouter(
    prefix="/nerdle",
)


def set_word_into_db(user_id: int, database: Session) -> None:
    """
    Set word into db
    """
    previous_word = (
        database.query(Nerdle.current_word)
        .filter(Nerdle.user_id == user_id)
        .first()[0]
    )
    word = random.choice(word_list)
    while previous_word == word:
        word = random.choice(word_list)
    database.query(Nerdle).filter(Nerdle.user_id == user_id).update(
        {"current_word": word}
    )
    database.commit()


@router.post(
    "/set_word",
    response_model=WordResponseModel,
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
)
async def set_word(
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
        )[0]
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
                current_word=random.choice(word_list),
                score=0,
                streak=0,
            )
            database.add(nerdle)
            database.commit()
        else:
            set_word_into_db(user_id=user_id, database=database)
        return WordResponseModel(status="Successful")
    except Exception as exception:
        logger.error(f"Error in get_word: {exception}")
        raise HTTPException(
            status_code=500,
            detail="Error Setting Word.",
            headers={"X-Error": "Error Setting word"},
        ) from exception
    except GenericError as exception:
        logger.error(f"Error in get_word: {exception}")
        raise HTTPException(
            status_code=400,
            detail="Error setting word.",
            headers={"X-Error": "Error in getting word"},
        ) from exception


@router.get(
    "/get_guesses",
    response_model=GuessesResponseModel,
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
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
            .first()[0]
        )
        if user_id is None:
            raise GenericError("User not found")
        guesses = (
            database.query(Guesses)
            .filter(Guesses.user_id == user_id)
            .order_by(Guesses.position.asc())
            .all()
        )
        return GuessesResponseModel(
            guesses=guesses,
        )
    except Exception as exception:
        logger.error(f"Error in get_guesses: {exception}")
        raise HTTPException(
            status_code=500,
            detail="Getting Guesses failed.",
            headers={"X-Error": "Error in getting guesses"},
        ) from exception
    except GenericError as exception:
        logger.error(f"Failed to get Guesses: {exception}")
        raise HTTPException(
            status_code=400,
            detail="Guess Validation Failed",
            headers={"X-Error": "Error Validating Guess"},
        ) from exception


@router.post(
    "/validate_guess/",
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
        )[0]
        if not user_id:
            raise GenericError("User not found")
        is_guess_valid = is_valid_word(word=unvalidated_guess.guess)
        if not is_guess_valid:
            raise GenericError("Invalid guess")
        answer = (
            database.query(Nerdle.current_word)
            .filter(Nerdle.user_id == user_id)
            .first()[0]
        )
        validated_guess_response: WinningGuessModel = (
            validate_guess_controller(
                answer=answer, unvalidated_guess=unvalidated_guess.guess
            )
        )
        guesses = (
            database.query(Guesses)
            .filter(Guesses.user_id == user_id)
            .all()
        )
        if validated_guess_response.is_win:
            nerdle = (
                database.query(Nerdle)
                .filter(Nerdle.user_id == user_id)
                .first()
            )
            nerdle.score += 1
            nerdle.streak += 1
            database.query(Guesses).filter(
                Guesses.user_id == user_id
            ).delete()
            set_word_into_db(user_id=user_id, database=database)
        elif len(guesses) == 5 and not validated_guess_response.is_win:
            nerdle = (
                database.query(Nerdle)
                .filter(Nerdle.user_id == user_id)
                .first()
            )
            nerdle.streak = 0
            database.query(Guesses).filter(
                Guesses.user_id == user_id
            ).delete()
            set_word_into_db(user_id=user_id, database=database)
        else:
            guess = Guesses(
                guess=unvalidated_guess.guess,
                user_id=user_id,
                position=len(guesses) + 1,
            )
            database.add(guess)
        database.commit()
        return GuessValidationResponseModel(
            validated_guess=validated_guess_response.validated_guess
        )
    except Exception as exception:
        logger.error(f"Failed to Validate Guess: {exception}")
        raise HTTPException(
            status_code=500,
            detail="Guess Validation Failed",
            headers={"X-Error": "Error Validating Guess"},
        ) from exception
    except GenericError as exception:
        logger.error(f"Failed to Validate Guess: {exception}")
        raise HTTPException(
            status_code=400,
            detail="Guess Validation Failed",
            headers={"X-Error": "Error Validating Guess"},
        ) from exception


@router.get(
    "/get_score",
    response_model=NerdleScoreResponseModel,
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
)
async def get_score(
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> NerdleScoreResponseModel:
    """
    GET route for getting score
    """
    try:
        email = decode_jwt(token)["user_email"]
        user_id = (
            database.query(Users.id).filter(Users.email == email).first()
        )[0]
        if not user_id:
            raise GenericError("User not found")
        nerdle = (
            database.query(Nerdle)
            .filter(Nerdle.user_id == user_id)
            .first()
        )
        return NerdleScoreResponseModel(
            score=nerdle.score,
            streak=nerdle.streak,
        )
    except Exception as exception:
        logger.error(f"Failed to get Score: {exception}")
        raise HTTPException(
            status_code=500,
            detail="Getting Score failed.",
            headers={"X-Error": "Error in getting score"},
        ) from exception
    except GenericError as exception:
        logger.error(f"Failed to get Score: {exception}")
        raise HTTPException(
            status_code=400,
            detail="Score Validation Failed",
            headers={"X-Error": "Error Validating Score"},
        ) from exception
