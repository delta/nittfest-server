"""
Events Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger

from server.controllers.event import (
    get_events,
    update_events,
    update_points,
)
from server.models.errors import GenericError
from server.models.event import ClusterModel, EventResponseModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point
from server.controllers.auth import JWTBearer, test_admin

router = APIRouter(prefix="/events")


@router.get(
    "/",
    dependencies=[Depends(get_database)],
    response_model=list[ClusterModel],
)
async def get_event(
    database: Session = Depends(get_database),
) -> list[ClusterModel]:
    """
    GET route for events
    """
    try:
        events = tuple(
            database.query(Event).order_by(Event.cluster_id).all()
        )
        cluster = tuple(
            database.query(Cluster).order_by(Cluster.id.asc()).all()
        )
        points = tuple(database.query(Point).all())
        departments = tuple(database.query(Department).all())

        return get_events(
            events=events,
            clusters=cluster,
            points=points,
            departments=departments,
        )

    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching events:{exception}",
        ) from exception


@router.post(
    "/update",
    dependencies=[Depends(get_database), Depends(JWTBearer())],
)
async def update_event(
    responses: ClusterModel,
    database: Session = Depends(get_database),
    token: str = Depends(JWTBearer()),
) -> EventResponseModel:
    """
    POST route for event updation
    """
    try:
        test_admin(token=token)
        update_events(events=responses.events[0], database=database)
        update_points(events=responses.events[0], database=database)
        return EventResponseModel(message="Events Updated Succesfully")
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while updating events:{Exception}",
        ) from Exception
