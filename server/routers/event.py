"""
Events Router
"""

from urllib import response
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
    # add Depends(JWTBearer()) after testing for JWT authentication
    dependencies=[Depends(get_database)],
)
async def update(
    responses: ClusterModel,
    database: Session = Depends(get_database),
):
    """
    POST route for events updation
    """
    try:
        for data in responses.events:
            events = data
            Event_data = database.query(Event).filter_by(
                name=events.name).first()
            Point_list = database.query(Point).filter_by(
                event_id=Event_data.id).all()

            for i in range(len(events.points)):
                Point_list[i].point = events.points[i].point
                Point_list[i].position = events.points[i].position
                DepartmentId = database.query(Department).filter_by(
                    name=events.points[i].department).first().id
                if DepartmentId == None:
                    DepartmentId = 0
                Point_list[i].department_id = DepartmentId

            Event_data.description = events.description
            Event_data.rules = events.rules
            Event_data.form_link = events.form_link
            Event_data.event_link = events.event_link
            Event_data.image_link = events.image_link
            Event_data.start_time = events.start_time
            Event_data.end_time = events.end_time
            Event_data.is_reg_completed = events.is_reg_completed
            Event_data.is_event_completed = events.is_event_completed
            print(Event_data)
            database.commit()

    except:
        raise GenericError("Invalid Token")
