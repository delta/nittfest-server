"""
Auth route
"""

import requests
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from config.settings import settings
from server.controllers.auth import check_auth, get_department_id, sign_jwt
from server.models.admin import AuthResponseModel
from server.schemas.users import Users

router = APIRouter(
    prefix="/auth",
)


@router.get("/callback/")
async def fetch_user_details(
    code: str, session: Session = Depends(get_database)
):
    """
    Handles the callback route and fetches the user details
    """

    params = {
        "client_id": settings.client_id,
        "client_secret": settings.client_secret,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.redirect_url,
    }
    try:
        token_response = requests.post(
            url=settings.token_endpoint, data=params
        ).json()
        logger.debug(token_response)
        headers = {
            "Authorization": "Bearer " + token_response["access_token"]
        }
        userdetails = requests.post(
            url=settings.resource_endpoint,
            headers=headers,
        ).json()
        if (
            not session.query(Users)
            .filter_by(email=userdetails["email"])
            .first()
        ):
            new_user = Users(
                name=userdetails["name"],
                email=userdetails["email"],
                mobile_number=userdetails["phoneNumber"],
                gender=userdetails["gender"],
                department_id=get_department_id(userdetails["email"]),
                fcm_token="123",
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
        logger.error(f"/dauth failed with {exception}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while authentication",
            headers={
                "X-Error": "An unexpected error occurred while authentication"
            },
        ) from exception


@router.post("/")
async def check(token: str):
    """
    Checks validity of token if in LocalStorage
    """

    auth_status = check_auth(token)
    return AuthResponseModel(isAuthorized=auth_status)
