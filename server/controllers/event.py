"""
Event controller
"""

from functools import lru_cache
from typing import List

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
