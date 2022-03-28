"""
parser route
"""
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from starlette.responses import FileResponse

from config.logger import logger
from config.settings import settings
from scripts.parser.parser import (
    generate_forms_responses,
    generate_preferences,
)
from server.controllers.auth import JWTBearer, decode_jwt
from server.models.admin import DownloadFormResponsesRequestModel
from server.models.errors import GenericError

router = APIRouter(
    prefix="/admin",
)


@router.post(
    "/downloadpreferences",
    dependencies=[Depends(JWTBearer())],
)
async def download_preferences(
    token: str = Depends(JWTBearer()),
) -> FileResponse:
    """
    Admin download preferences
    """
    try:
        email = decode_jwt(token)["user_email"]
        is_admin = bool(email in settings.admin)
        if not is_admin:
            raise GenericError("Not Admin")
        filepath = await generate_preferences()
        return FileResponse(filepath)
    except GenericError as exception:
        logger.error(f"{email} attempted to download responses")
        raise HTTPException(
            status_code=400,
            detail=f"{exception}",
        ) from exception


@router.post(
    "/downloadresponses",
    dependencies=[Depends(JWTBearer())],
)
async def download_responses(
    request_responses: DownloadFormResponsesRequestModel,
    token: str = Depends(JWTBearer()),
) -> FileResponse:
    """
    Admin download form responses
    """
    try:
        email = decode_jwt(token)["user_email"]
        is_admin = bool(email in settings.admin)
        if not is_admin:
            raise GenericError("Not Admin")
        filepath = await generate_forms_responses(
            request_responses.domain, request_responses.year
        )
        return FileResponse(filepath)
    except GenericError as exception:
        logger.error(f"{email} attempted to download responses")
        raise HTTPException(
            status_code=400,
            detail=f"{exception}",
        ) from exception
