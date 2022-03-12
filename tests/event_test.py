"""
Tests for event route
"""
from fastapi.testclient import TestClient

ROUTE = "/events"
res = [
    {
        "cluster": "Arts",
        "events": [
            {
                "name": "Art Event 1",
                "description": "Art Something",
                "rules": "free play",
                "form_link": "http://genericlink.com/route",
                "event_link": "http://genericlink.com/route",
                "image_link": "http://genericlink.com/route",
                "start_time": "start time",
                "end_time": "end time",
                "date": "date",
                "is_reg_completed": False,
                "is_event_completed": False,
                "points": [
                    {"point": 10, "position": 1, "department": "MME"},
                    {"point": 9, "position": 2, "department": "EEE"},
                    {"point": 0, "position": 3, "department": "ICE"},
                ],
            },
            {
                "name": "Art Event 2",
                "description": "Art Something",
                "rules": "free play",
                "form_link": "http://genericlink.com/route",
                "event_link": "http://genericlink.com/route",
                "image_link": "http://genericlink.com/route",
                "start_time": "start time",
                "end_time": "end time",
                "date": "date",
                "is_reg_completed": False,
                "is_event_completed": False,
                "points": [
                    {"point": 20, "position": 1, "department": "ICE"},
                    {"point": 10, "position": 2, "department": "EEE"},
                    {"point": 5, "position": 3, "department": "MME"},
                ],
            },
        ],
    },
    {
        "cluster": "Gaming",
        "events": [
            {
                "name": "Gaming Event 1",
                "description": "Game Something",
                "rules": "free play",
                "form_link": "http://genericlink.com/route",
                "event_link": "http://genericlink.com/route",
                "image_link": "http://genericlink.com/route",
                "start_time": "start time",
                "end_time": "end time",
                "date": "date",
                "is_reg_completed": False,
                "is_event_completed": False,
                "points": [
                    {"point": 10, "position": 1, "department": "MME"},
                    {"point": 9, "position": 2, "department": "EEE"},
                    {"point": 8, "position": 3, "department": "ICE"},
                ],
            },
            {
                "name": "Gaming Event 2",
                "description": "Game Something",
                "rules": "free play",
                "form_link": "http://genericlink.com/route",
                "event_link": "http://genericlink.com/route",
                "image_link": "http://genericlink.com/route",
                "start_time": "start time",
                "end_time": "end time",
                "date": "date",
                "is_reg_completed": False,
                "is_event_completed": False,
                "points": [
                    {"point": 10, "position": 1, "department": "ICE"},
                    {"point": 9, "position": 2, "department": "MME"},
                    {"point": 5, "position": 3, "department": "EEE"},
                ],
            },
        ],
    },
]


def get_events(client: TestClient):
    """
    get list of events
    """
    get_response = client.get(url=ROUTE)
    assert get_response.status_code == 200
    print(get_response.json())
    assert get_response.json() == res
