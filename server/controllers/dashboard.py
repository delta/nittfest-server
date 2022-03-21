"""
Dashboard controller
"""

from datetime import datetime

from server.models.event import EventModel
from server.schemas.event import Event


def get_upcoming_events(events: tuple[Event]) -> list[EventModel]:
    """
    Util function to get upcoming events
    """
    upcoming_events: list[EventModel] = []
    current_time = datetime.now()
    for event in events:
        if event.start_time > current_time:
            upcoming_events.append(
                EventModel(
                    image_link=event.image_link,
                    rules=event.rules,
                    description=event.description,
                    start_time=event.start_time,
                    end_time=event.end_time,
                    is_reg_completed=event.is_reg_completed,
                    name=event.name,
                    points=[],
                    form_link=event.form_link,
                    is_event_completed=event.is_event_completed,
                    event_link=event.event_link,
                )
            )
    return upcoming_events


def get_points(points: list[tuple], department: int) -> int:
    """
    Util function to get points of the department
    """
    point_list: dict = {}
    for point in points:
        point_list.update({point[0]: point[1]})
    print(point_list)
    return point_list.get(department, 0)


def get_position(points: list[tuple], department: int) -> int:
    """
    Util function to get position of the department
    """
    point_list: dict = {}
    for point in points:
        point_list.update({point[0]: point[1]})
    sorted_list = sorted(point_list.items(), key=lambda item: item[1])
    sorted_list.reverse()
    pos = 0
    current_value = -1
    for point in sorted_list:
        if current_value != point[1]:
            current_value = point[1]
            pos += 1
        if point[0] == department:
            break
    return pos
