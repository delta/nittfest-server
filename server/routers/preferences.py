"""
Preference router.
"""
from fastapi import APIRouter, Depends

from server.schemas.users import Users
from server.models.preferences import PreferenceResponseModel
from server.schemas.preferences import Preferences
from server.controllers.auth import JWTBearer, decode_jwt
from server.config.database import SessionLocal

router = APIRouter(
    prefix="/preferences",
)


@router.get(
    "/",
    response_model=PreferenceResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def preferences(
    token: str = Depends(JWTBearer()),
) -> PreferenceResponseModel:
    """
    GET route for preferences
    """
    database = SessionLocal()
    email = decode_jwt(token)["user_email"]
    user = database.query(Users).filter_by(email=email).first()
    user_preferences = database.query(Preferences).filter_by(
        user_id=user.id
    )

    preferences_response = []

    for preference in user_preferences:
        preferences_response.append(preference.preference_no)

    return preferences_response
