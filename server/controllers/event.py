"""
Event controller
"""

from typing import List

from server.models.event import ClusterModel, EventModel, PointModel
from server.schemas.cluster import Cluster
from server.schemas.event import Event


def get_events(
    events: list[Event], clusters: list[Cluster], points: list
) -> list[ClusterModel]:
    """
    Util function to make response
    """
    points_list = {}
    for point in points:
        value = points_list.get(point[0].event_id, [])
        value.append(
            PointModel(
                point=point[0].point,
                position=point[0].position,
                department=point[1].name,
            )
        )
        points_list.update({point[0].event_id: value})
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
                date=event.date,
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
