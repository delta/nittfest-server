"""
Auth controllers
"""
import jwt as JWT
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from config.logger import logger
from config.settings import settings

jwt_secret = settings.jwt_secret
jwt_algo = settings.jwt_algo


def jwt_response(token: str):
    """
    Util function to return the token
    """
    logger.debug(f"Returning JWT for {token}")
    return {"jwt_token": token}


def sign_jwt(user_email: str, user_name: str) -> dict[str, str]:
    """
    Function to Generate The Token
    """
    logger.debug(f"Signing JWT for {user_email}")
    payload = {
        "user_email": user_email,
        "user_name": user_name,
    }
    token = JWT.encode(payload=payload, key=jwt_secret, algorithm=jwt_algo)

    return jwt_response(token)


def decode_jwt(token: str) -> dict:
    """
    Function to Decode The JWT
    """
    logger.debug(f"Decoding JWT for {token}")
    try:
        decoded_token = JWT.decode(
            token, jwt_secret, algorithms=[jwt_algo]
        )
        return decoded_token
    except Exception as exception:
        logger.error(f"Error Decoding JWT: {exception}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized Access: JWT Invalid",
        ) from exception


def verify_jwt(jwtoken: str) -> bool:
    """
    Verify the JWT Token
    """
    is_token_valid: bool = False

    try:
        payload = decode_jwt(jwtoken)
    except Exception as exception:
        logger.error(f"Invalid JWT Token: {jwtoken}")
        payload = None
        raise HTTPException(
            status_code=403,
            detail="Invalid token or expired token.",
        ) from exception

    if payload:
        is_token_valid = True
    return is_token_valid


def get_department_id(email: str) -> int:
    """
    get the department id of the current User
    """
    if int(email[0] == 1):
        return int(email[1:3])
    if int(email[0] == 2):
        return 15
    if int(email[0] == 3 or email[0] == 4):
        return 16

    return 1


class JWTBearer(HTTPBearer):
    """
    JWT Bearer Authentication
    """

    def __init__(self, auto_error: bool = True):
        """
        Initialize the JWT Bearer Authentication
        """
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        Call the JWT Bearer Authentication
        """
        credentials: HTTPAuthorizationCredentials = await super().__call__(
            request
        )
        try:
            if not credentials.scheme == "Bearer":
                logger.error(f"Invalid JWT Scheme: {credentials.scheme}")
                raise HTTPException(
                    status_code=403,
                    detail="Invalid authentication scheme.",
                )
            if not verify_jwt(credentials.credentials):
                logger.error(
                    f"Invalid JWT Token: {credentials.credentials}"
                )
                raise HTTPException(
                    status_code=403,
                    detail="Invalid token or expired token.",
                )
            return credentials.credentials
        except Exception as exception:
            logger.error("Invalid Authorization code due to: {exception}")
            raise HTTPException(
                status_code=403, detail="Invalid authorization code."
            ) from exception
