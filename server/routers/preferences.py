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
) -> PreferenceResponseModel:
    """
    GET route for preferences
    """
    database = SessionLocal()
    _email = decode_jwt(token)["user_email"]
    _user = database.query(Users).filter_by(email=_email).first()

    return {
        "status": bool(
            database.query(Preferences).filter_by(user_id=_user.id).count()
        )
    }


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

        for i in range(1, 7):
            if (
                database.query(Preferences)
                .filter_by(user_id=user.id, preference_no=i)
                .count()
            ):
                database.query(Preferences).filter_by(
                    user_id=user.id, preference_no=i
                ).delete()
        database.add(Preferences(user.id, 1, preferences.preference_1))
        database.add(Preferences(user.id, 2, preferences.preference_2))
        database.add(Preferences(user.id, 3, preferences.preference_3))
        database.add(Preferences(user.id, 4, preferences.preference_4))
        database.add(Preferences(user.id, 5, preferences.preference_5))
        database.add(Preferences(user.id, 6, preferences.preference_6))
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
