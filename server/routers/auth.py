"""
Auth route
"""

import requests
from fastapi import APIRouter, HTTPException
from server.config.settings import settings
from server.schemas.users import Users

from server.config.database import SessionLocal
from server.controllers.auth import sign_jwt
from server.config.logger import logger

router = APIRouter(
    prefix="/auth",
)


@router.get("/callback/")
async def fetch_user_details(
    code: str,
):
    """
    Handles the callback route and fetches the user details
    """
    auth_code = code

    client_id = settings.client_id
    client_secret = settings.client_secret
    redirect_url = settings.redirect_url
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_url,
    }
    try:
        token_response = requests.post(
            url="https://auth.delta.nitt.edu/api/oauth/token", data=params
        ).json()
        headers = {
            "Authorization": "Bearer " + token_response["access_token"]
        }
        userdetails = requests.post(
            url="https://auth.delta.nitt.edu/api/resources/user",
            headers=headers,
        ).json()
        session = SessionLocal()
        if (
            not session.query(Users)
            .filter_by(email=userdetails["email"])
            .first()
        ):
            new_user = Users(
                userdetails["name"],
                userdetails["email"],
                userdetails["phoneNumber"],
                userdetails["gender"],
            )
            session.add(new_user)
            session.commit()
        session.close()
        jwt = sign_jwt(userdetails["email"], userdetails["name"])
        logger.info(f'{userdetails["name"]} user logged in')
        return {
            "name": userdetails["name"],
            "email": userdetails["email"],
            "phoneNumber": userdetails["phoneNumber"],
            "gender": userdetails["gender"],
            "jwt": jwt["jwt_token"],
        }
    except Exception as exception:
        logger.error("/dauth failed with {exception}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while authentication",
            headers={"X-Error": str(exception)},
        ) from exception
