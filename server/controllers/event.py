"""
Event controller
"""

from server.models.event import ClusterModel, EventModel, PointModel
from server.schemas.cluster import Cluster
from server.schemas.event import Event
from server.schemas.point import Point


def make_reponse(
    events: list[Event], clusters: list[Cluster], points: list[Point]
) -> list[ClusterModel]:
    """
    Util function to make response
    """
    response: list[ClusterModel] = []
    index: int = 0
    for cluster in clusters:
        event_list: list[EventModel] = []
        while index < len(events):
            event = events[index]
            if event.cluster_id == cluster.id:
                points_list: list[PointModel] = []
                for point in points:
                    if point[0].event_id == event.id:
                        points_list.append(
                            PointModel(
                                point=point[0].point,
                                position=point[0].position,
                                department=point[1].name,
                            )
                        )
                event_list.append(
                    EventModel(
                        name=event.name,
                        points=points_list,
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
                index += 1
            else:
                break
        response.append(
            ClusterModel(cluster=cluster.name, events=event_list)
        )
    return response
