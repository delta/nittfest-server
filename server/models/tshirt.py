"""
Tshirt Registration Modals
"""

from pydantic import BaseModel
from pydantic.fields import Field


class TshirtRequestModel(BaseModel):
    """Request model for Tshirt"""

    size: str = Field(
        ...,
        title="Size",
        description="Size of the tshirt",
    )


class TshirtResponseModel(BaseModel):
    """Response model for Tshirt"""

    message: str = Field(
        ...,
        title="Tshirt Registration Status",
        description="Response message for registration status",
    )
