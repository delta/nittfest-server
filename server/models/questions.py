"""
Models for the questions.
"""

from pydantic import BaseModel
from pydantic.fields import Field


class DomainModel(BaseModel):
    """
    Request model for domain
    """

    domain: str = Field(
        ...,
        title="Domain of Question",
        description="Domain for which the questions are needed",
    )


class DomainResponseModel(BaseModel):
    """
    Response model for domain
    """

    questions: list = Field(
        ..., title="Questions", description="List of questions"
    )
