"""
Preference router.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.controllers.auth import JWTBearer, decode_jwt
from server.controllers.preferences import (
    check_duplicate_preferences,
    get_preferences_by_id,
    validate_preferences,
)
from server.models.errors import GenericError
from server.models.preferences import (
    PreferenceRequestModel,
    PreferenceResponseModel,
)
from server.schemas.preferences import Preferences
from server.schemas.users import Users

router = APIRouter(
    prefix="/preferences",
)


@router.get(
    "/",
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
)
async def check_preferences(
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> PreferenceResponseModel:
    """
    GET route for preferences
    """
    try:
        email = decode_jwt(token)["user_email"]
        user = database.query(Users).filter_by(email=email).first()
        if not user:
            raise GenericError("User Not found")
        return {
            "status": bool(
                database.query(Preferences)
                .filter_by(user_id=user.id)
                .count()
            )
        }
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"{exception}",
        ) from exception


@router.post(
    "/",
    dependencies=[Depends(JWTBearer()), Depends(get_database)],
)
async def post_preferences(
    preferences: PreferenceRequestModel,
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> PreferenceResponseModel:
    """
    Post route for preferences
    """
    try:
        email = decode_jwt(token)["user_email"]
        yearcode = email.split("@")[0]
        isfirstyear = bool(yearcode[5] == "1")
        if not isfirstyear:
            raise GenericError("User Not First-Year")
        user = database.query(Users).filter_by(email=email).first()
        if not user:
            raise GenericError("User Not found")

        pref_ids = get_preferences_by_id(
            preferences=preferences.preferences, database=database
        )

        if validate_preferences(pref_ids):
            raise GenericError("Prior-Preference is not filled")

        if check_duplicate_preferences(pref_ids):
            raise GenericError("Duplicate Entries Found")

        for i, pref in enumerate(pref_ids):
            if (
                not database.query(Preferences)
                .filter_by(user_id=user.id, preference_no=i + 1)
                .count()
            ):
                database.add(
                    Preferences(
                        user_id=user.id,
                        preference_no=i + 1,
                        domain_id=pref,
                    )
                )

            else:
                raise GenericError("Preferences Already Filled")
        database.query(Users).filter_by(id=user.id).update(
            dict(prefered_email=preferences.email)
        )
        logger.info(f"{email} form preferences submitted")
        return {"status": True}

    except GenericError as exception:
        logger.error(
            f"{email} Preferences submission failed due to {exception}"
        )
        raise HTTPException(
            status_code=403,
            detail=f"{exception}",
        ) from exception
