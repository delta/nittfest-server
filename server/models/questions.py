"""
Models for the questions.
"""

from pydantic import BaseModel
from pydantic.fields import Field


class QuestionRequestModel(BaseModel):
    """
    Request model for domain
    """

    domain: str = Field(
        ...,
        title="Domain of Question",
        description="Domain for which the questions are needed",
    )


class QuestionResponseModel(BaseModel):
    """
    Response model for domain
    """

    questions: list = Field(
        ..., title="Questions", description="List of questions"
    )


class AnswerRequestModel(BaseModel):
    """
    Request model for answer
    """

    answers: list = Field(
        ...,
        title="Answer",
        description="Answer for the question",
    )

    preference_no: int = Field(
        ...,
        title="Preference",
        description="Preference number",
    )

    domain: str = Field(
        ...,
        title="Domain",
        description="Domain of the question",
    )


class AnswerResponseModel(BaseModel):
    """
    Response model for answer
    """

    message: str = Field(
        ...,
        title="Answer",
        description="Response model Answer for the question",
    )
