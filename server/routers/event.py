"""
Events Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from config.settings import settings

from server.controllers.event import get_events, update_events
from server.models.errors import GenericError
from server.models.event import ClusterModel, EventResponseModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point
from server.controllers.auth import JWTBearer, decode_jwt

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
    "/",
    dependencies=[Depends(get_database), Depends(JWTBearer())],
)
async def update(
    responses: ClusterModel,
    database: Session = Depends(get_database),
    token: str = Depends(JWTBearer()),
) -> EventResponseModel:
    """
    POST route for events updation
    """
    try:
        email = decode_jwt(token)["user_email"]
        is_admin = bool(email in settings.admin)
        if not is_admin:
            raise GenericError("Not Admin")
        update_events(events_list=responses.events, database=database)
        return EventResponseModel(message="Events Updated Succesfully")
    except:
        raise GenericError("Invalid Token")
