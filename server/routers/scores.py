"""
Scores Router
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from frozendict import frozendict

from server.schemas.point import Point
from server.schemas.department import Department
from server.schemas.cluster import Cluster
from server.schemas.event import Event
from server.controllers.scores import get_all_scores
from server.models.scores import ScoreModel
from server.models.errors import GenericError
from config.database import get_database
from config.logger import logger

router = APIRouter(prefix="/scores")


@router.get(
    "/",
    dependencies=[Depends(get_database)],
    response_model=list[ScoreModel],
)
async def get_scores(
    database: Session = Depends(get_database),
) -> list[ScoreModel]:
    """
    GET route for scores
    """
    try:
        clusters = database.query(Cluster).order_by(Cluster.id.asc()).all()
        departments = database.query(Department).all()
        points = (
            database.query(Point, Event)
            .order_by(Point.event_id.asc())
            .join(Event, Event.id == Point.event_id)
            .all()
        )
        dept_list: dict = {}
        cluster_list: dict = {}

        for dept in departments:
            dept_list.update({dept.id: dept.name})

        for cluster in clusters:
            cluster_list.update({cluster.id: cluster.name})
        return get_all_scores(
            dept_list=frozendict(dept_list),
            cluster_list=frozendict(cluster_list),
            points=tuple(points),
        )
    except GenericError as exception:
        logger.error(f"Fetching Events failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching events:{exception}",
        ) from exception
