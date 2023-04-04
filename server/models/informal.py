"""
Event Model
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic.fields import Field


class InformalModel(BaseModel):
    """Model for events"""

    name: str = Field(..., title="name", description="name of the event")
    description: str = Field(
        ..., title="description", description="description of the event"
    )
    cluster_id: int = Field(
        ..., title="cluster_id", description="cluster_id of the event"
    )
    rules: str = Field(
        ..., title="rules", description="Rules of the event"
    )
    form_link: str = Field(
        ..., title="Form Link", description="Link for registering"
    )
    informal_link: str = Field(
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
    venue: str = Field(
        ..., title="Venue", description="Venue of the event"
    )
    is_reg_completed: bool = Field(
        ..., title="is Filled", description="Checks registration deadline"
    )
    is_informal_completed: bool = Field(
        ..., title="is Completed", description="Checks if informal is completed"
    )

class ClusterModel(BaseModel):
    """Model for cluster"""
    informals: list[InformalModel] = Field(
        ...,
        title="informal",
        description="List of informals under this cluster",
    )

class InformalResponseModel(BaseModel):
    """Response model for Updating Events"""

    message: str = Field(
        ...,
        title="Update Status",
        description="Response message for Updation status",
    )

class InformalRegisterRequestModel(BaseModel):
    """Request model for registering events"""

    informal_name: str
