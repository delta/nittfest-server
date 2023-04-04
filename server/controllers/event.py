"""
Event controller
"""

from functools import lru_cache
from typing import List

from sqlalchemy.orm import Session
from server.models.errors import GenericError
from server.models.event import ClusterModel, EventModel, PointModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point


@lru_cache()
def get_events(
    events: tuple[Event],
    clusters: tuple[Cluster],
    points: tuple[Point],
    departments: tuple[Department],
) -> list[ClusterModel]:
    """
    Util function to make response
    """
    points_list = {}
    department_list = {}
    for department in departments:
        department_list.update({department.id: department.name})
    for point in points:
        value = points_list.get(point.event_id, [])
        value.append(
            PointModel(
                point=point.point,
                position=point.position,
                department=department_list.get(point.department_id, "N/A"),
            )
        )
        points_list.update({point.event_id: value})
    event_list = {}
    for event in events:
        value = event_list.get(event.cluster_id, [])
        value.append(
            EventModel(
                name=event.name,
                points=points_list.get(event.id, []),
                rules=event.rules,
                format=event.format,
                resources=event.resources,
                description=event.description,
                form_link=event.form_link,
                image_link=event.image_link,
                start_time=event.start_time,
                end_time=event.end_time,
                is_reg_completed=event.is_reg_completed,
                is_event_completed=event.is_event_completed,
                event_link=event.event_link,
            )
        )
        event_list.update({event.cluster_id: value})
    response: List[ClusterModel] = []
    for cluster in clusters:
        response.append(
            ClusterModel(
                cluster=cluster.name, events=event_list.get(cluster.id, [])
            )
        )
    return response


def update_events(events: EventModel, database: Session):
    """
    Util function to update events
    """
    event_data = database.query(Event).filter_by(name=events.name).first()
    if not event_data:
        raise GenericError("Event Does not exist")

    event_data.description = events.description
    event_data.rules = events.rules
    event_data.format = events.format
    event_data.resources = events.resources
    event_data.form_link = events.form_link
    event_data.event_link = events.event_link
    event_data.image_link = events.image_link
    event_data.start_time = events.start_time
    event_data.end_time = events.end_time
    event_data.is_reg_completed = events.is_reg_completed
    event_data.is_event_completed = events.is_event_completed
    database.commit()


def update_points(events: EventModel, database: Session):
    """
    Util function to update points
    """
    event_data = database.query(Event).filter_by(name=events.name).first()
    point_list = (
        database.query(Point).filter_by(event_id=event_data.id).all()
    )

    if len(events.points) != len(point_list):
        raise GenericError("Number of points does not match")

    for index, item in enumerate(point_list):
        item.point = events.points[index].point
        item.position = events.points[index].position
        department_id = (
            database.query(Department)
            .filter_by(name=events.points[index].department)
            .first()
            .id
        )
        if department_id is None:
            raise GenericError("Invalid Department")
        item.department_id = department_id
    database.commit()
