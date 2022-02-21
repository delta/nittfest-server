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
