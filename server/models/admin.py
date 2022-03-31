"""
Admin model
"""


from pydantic import BaseModel
from pydantic.fields import Field


class DownloadFormResponsesRequestModel(BaseModel):
    """
    Response model for preferences
    """

    domain: str = Field(
        ...,
        title="Domain",
        description="Domain of form response that needs to be downloaded",
    )
    year: int = Field(
        ...,
        title="year",
        description="year students's form response that needs to be downloaded",
    )


class LoginRequestModel(BaseModel):
    """
    Response model for Authentication
    """

    roll_number: str = Field(
        ...,
        title="Roll Number",
        description="Roll Number of user that needs to be logged in",
    )
    password: str = Field(
        ...,
        title="Password",
        description="Password of user that needs to be logged in",
    )


class AdminResponseModel(BaseModel):
    """
    Response model for admin
    """

    isAuthorized: str = Field(
        ...,
        title="Message",
        description="Message to be displayed to user",
    )
    jwt_token: str = Field(
        ...,
        title="JWT Token",
        description="JWT Token to be sent to user",
    )


class AuthResponseModel(BaseModel):
    """
    Response model for Authentication
    """

    isAuthorized: bool = Field(
        ...,
        title="Check Authentication",
        description="Authentication Status",
    )
