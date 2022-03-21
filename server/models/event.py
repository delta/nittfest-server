"""
Event Model
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic.fields import Field


class PointModel(BaseModel):
    """
    model for point
    """

    point: float = Field(
        ..., title="point", description="score of the event"
    )

    position: int = Field(
        ...,
        title="description",
        description="current positon in the event",
    )

    department: str = Field(
        ...,
        title="department",
        description="department in that current position",
    )


class EventModel(BaseModel):
    """Model for events"""

    name: str = Field(..., title="name", description="name of the event")
    description: str = Field(
        ..., title="description", description="description of the event"
    )
    rules: str = Field(
        ..., title="rules", description="Rules of the event"
    )
    form_link: str = Field(
        ..., title="Form Link", description="Link for registering"
    )
    event_link: str = Field(
        ..., title="Event Link", description="link of the event"
    )
    image_link: str = Field(
        ..., title="Image Link", description="logo of the event"
    )
    start_time: datetime = Field(
        ..., title="Start Time", description="Start Time of the event"
    )
    end_time: datetime = Field(
        ..., title="End Time", description="End Time of the event"
    )
    is_reg_completed: bool = Field(
        ..., title="is Filled", description="Checks registration deadline"
    )
    is_event_completed: bool = Field(
        ..., title="is Completed", description="Checks if event completed"
    )
    points: list[PointModel] = Field(
        ..., title="points", description="array of points"
    )


class ClusterModel(BaseModel):
    """Model for cluster"""

    cluster: str = Field(
        ...,
        title="cluster",
        description="Name of the cluster the vent belongs to",
    )
    events: list[EventModel] = Field(
        ...,
        title="events",
        description="List of events under this cluster",
    )
