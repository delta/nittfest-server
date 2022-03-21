"""

Nerdle Models
"""

from pydantic import BaseModel
from pydantic.fields import Field


class GuessesResponseModel(BaseModel):
    """
    Guesses Response Model
    """

    guesses: list = Field(
        ...,
        title="List of Guesses",
        description="List of all current guesses made by user",
    )


class WordResponseModel(BaseModel):
    """
    Word Response Model
    """

    status: str = Field(
        ...,
        title="Current Word Set Status",
        description="Status of setting the current word being guesses",
    )


class GuessValidationRequestModel(BaseModel):
    """
    Model for Guess Validation
    """

    guess: str = Field(
        ...,
        title="Guess Validation",
        description="Guess Validation for Single guess",
    )


class GuessValidationResponseModel(BaseModel):
    """
    Guess Validation Response Model
    """

    validated_guess: list = Field(
        ...,
        title="Validated Guess",
        description="Guess with letters validated",
    )


class WinningGuessModel(BaseModel):
    """
    Model for Nerdle controller to return if a guess is correct
    """

    validated_guess: list = Field(
        ...,
        title="Validated Guess",
        description="Guess which is validated",
    )

    is_win: bool = Field(
        ...,
        title="Is Winning Guess?",
        description="Is the current guess right?",
    )


class NerdleScoreResponseModel(BaseModel):
    """
    Nerdle Score Response Model
    """

    score: int = Field(
        ...,
        title="Nerdle Score",
        description="Current Nerdle Score",
    )

    streak: int = Field(
        ...,
        title="Nerdle Streak",
        description="Current Nerdle Streak",
    )
