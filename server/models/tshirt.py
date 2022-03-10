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
