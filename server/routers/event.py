"""
Events Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.controllers.event import get_events
from server.models.errors import GenericError
from server.models.event import ClusterModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point

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
        events = database.query(Event).order_by(Event.cluster_id).all()
        cluster = database.query(Cluster).order_by(Cluster.id.asc()).all()
        points = (
            database.query(Point, Department)
            .order_by(Point.position.asc())
            .join(Department, Department.id == Point.department_id)
            .all()
        )
        return get_events(events=events, clusters=cluster, points=points)

    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching events:{exception}",
        ) from exception
