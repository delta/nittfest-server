"""
Preferences model
"""


from pydantic import BaseModel
from pydantic.fields import Field


class PreferenceResponseModel(BaseModel):
    """
    Response model for preferences
    """

    status: bool = Field(
        ..., title="Status", description="Status of preference submission"
    )


class PreferenceRequestModel(BaseModel):
    """
    Request Model for Preferences
    """

    email: str = Field(
        ...,
        title="Email",
        description="Prefered emailID for the user",
    )
    preferences: list = Field(
        [None] * 3,
        title="Preferences",
        description="Preferences of the user",
    )
