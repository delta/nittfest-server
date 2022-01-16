"""
Auth route
"""


import requests
import jwt as JWT
from fastapi import APIRouter, HTTPException, status
from server.config.settings import settings
from server.schemas.users import Users

from server.config.database import SessionLocal


router = APIRouter(
    prefix="/auth",
)

jwt_secret = settings.jwt_secret
jwt_algo = settings.jwt_algo


def jwt_response(token: str):
    """
    Util function to return the token
    """
    return {"jwt_token": token}


def sign_jwt(user_email: str, user_name: str) -> dict[str, str]:
    """
    Function to Generate The Token
    """
    payload = {
        "user_email": user_email,
        "user_name": user_name,
    }
    token = JWT.encode(payload, jwt_secret, algorithm=jwt_algo)

    return jwt_response(token)


def decode_jwt(token: str) -> dict:
    """
    Function to Decode The JWT
    """
    try:
        decoded_token = JWT.decode(
            token, jwt_secret, algorithms=[jwt_algo]
        )
        return decoded_token
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Access: JWT Invalid",
        ) from exception


@router.get("/callback/")
async def fetch_user_details(
    code: str,
):
    """Handles the callback route and fetches the user details"""
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
    token_response = requests.post(
        url="https://auth.delta.nitt.edu/api/oauth/token", data=params
    ).json()
    headers = {"Authorization": "Bearer " + token_response["access_token"]}
    userdetails = requests.post(
        url="https://auth.delta.nitt.edu/api/resources/user",
        headers=headers,
    ).json()
    new_user = Users(
        userdetails["name"],
        userdetails["email"],
        userdetails["phoneNumber"],
        userdetails["gender"],
    )
    session = SessionLocal()
    session.add(new_user)
    session.commit()
    jwt = sign_jwt(userdetails["email"], userdetails["name"])
    return {
        "name": userdetails["name"],
        "email": userdetails["email"],
        "phoneNumber": userdetails["phoneNumber"],
        "gender": userdetails["gender"],
        "jwt": jwt["jwt_token"],
    }
