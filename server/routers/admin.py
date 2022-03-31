"""
parser route
"""
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from starlette.responses import FileResponse

from config.settings import settings
from scripts.parser.parser import (
    generate_forms_responses,
    generate_preferences,
)
from server.controllers.auth import (
    JWTBearer,
    sign_jwt_auth,
    test_admin,
)
from server.models.admin import (
    AdminResponseModel,
    DownloadFormResponsesRequestModel,
    LoginRequestModel,
)
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
        test_admin(token)
        filepath = await generate_preferences()
        return FileResponse(filepath)
    except GenericError as exception:
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
        test_admin(token)
        filepath = await generate_forms_responses(
            request_responses.domain, request_responses.year
        )
        return FileResponse(filepath)
    except GenericError as exception:
        raise HTTPException(
            status_code=400,
            detail=f"{exception}",
        ) from exception


@router.post("/")
def event_jwt(response: LoginRequestModel):
    """
    Admin login for events
    """
    if response.roll_number == settings.admin_roll:
        jwt_res = sign_jwt_auth(roll=response.roll_number)
        return AdminResponseModel(
            isAuthorized=True, jwt_token=jwt_res["jwt_token"]
        )
    return AdminResponseModel(isAuthorized=False, jwt_token="")
