"""
Preferences model
"""


from pydantic import BaseModel


class PreferenceResponseModel(BaseModel):
    """
    Response model for preferences
    """

    preference_no: int
    domain: str
