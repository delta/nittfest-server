"""
Preference router.
"""

from fastapi import APIRouter, HTTPException, Depends

from server.schemas.users import Users
from server.models.preferences import (
    PreferenceResponseModel,
    PreferenceRequestModel,
)
from server.models.errors import GenericError
from server.schemas.preferences import Preferences
from server.controllers.auth import JWTBearer, decode_jwt
from server.config.database import SessionLocal
from server.config.logger import logger

router = APIRouter(
    prefix="/preferences",
)


@router.get(
    "/",
    dependencies=[Depends(JWTBearer())],
)
async def check_preferences(
    token: str = Depends(JWTBearer()),
):
    """
    GET route for preferences
    """
    database = SessionLocal()
    _email = decode_jwt(token)["user_email"]
    _user = database.query(Users).filter_by(email=_email).first()

    return bool(
        database.query(Preferences).filter_by(user_id=_user.id).count()
    )


@router.post(
    "/",
    dependencies=[Depends(JWTBearer())],
)
async def post_preferences(
    preferences: PreferenceRequestModel,
    token: str = Depends(JWTBearer()),
) -> PreferenceResponseModel:
    """
    Post route for preferences
    """
    try:
        email = decode_jwt(token)["user_email"]
        database = SessionLocal()
        user = database.query(Users).filter_by(email=email).first()
        if not user:
            database.close()
            raise GenericError("User Not found")

        if (
            database.query(Preferences)
            .filter_by(user_id=user.id, preference_no=1)
            .count()
        ):
            database.query(Preferences).filter_by(
                user_id=user.id, preference_no=1
            ).delete()

        if (
            database.query(Preferences)
            .filter_by(user_id=user.id, preference_no=2)
            .count()
        ):
            database.query(Preferences).filter_by(
                user_id=user.id, preference_no=2
            ).delete()

        if (
            database.query(Preferences)
            .filter_by(user_id=user.id, preference_no=3)
            .count()
        ):
            database.query(Preferences).filter_by(
                user_id=user.id, preference_no=3
            ).delete()

        new_preference_1 = Preferences(
            user.id, 1, preferences.preference_1
        )
        new_preference_2 = Preferences(
            user.id, 2, preferences.preference_2
        )
        new_preference_3 = Preferences(
            user.id, 3, preferences.preference_3
        )
        database.add(new_preference_1)
        database.add(new_preference_2)
        database.add(new_preference_3)
        database.commit()
        database.close()
        logger.info(f"{email} form preferences submitted")
        return {"status": True}

    except GenericError as exception:
        logger.error(
            f"{email} Preferences submission failed due to {exception}"
        )
        raise HTTPException(
            status_code=403,
            detail="User not found",
        ) from exception
