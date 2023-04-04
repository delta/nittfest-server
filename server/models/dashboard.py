"""
Dasnboard Model
"""

from pydantic import BaseModel
from pydantic.fields import Field

from server.models.event import EventModel


class DashboardResponseModel(BaseModel):
    """
    model for dashboard
    """

    # department: str = Field(
    #     ...,
    #     title="department",
    #     description="department of the current User",
    # )

    # point: float = Field(
    #     ...,
    #     title="point",
    #     description="Total score of department in the event",
    # )

    # position: int = Field(
    #     ...,
    #     title="description",
    #     description="current positon of the department in the event",
    # )

    # upcoming_events: list[EventModel] = Field(
    #     ...,
    #     title="Upcomind Events",
    #     description="List of all upcoming Events",
    # )

    events: list[EventModel] = Field(
        ...,
        title="Registered Events",
        description="List of all registered events"
	)
    
    roll_no: str = Field(
        ...,
        title="Roll Number",
        description="Roll number"
	)
    
    name: str = Field(
        ...,
        title="Name",
        description="Name"
	)
