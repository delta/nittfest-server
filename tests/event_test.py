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
                "name": "dominoes",
                "description": "abc",
                "rules": "abc",
                "form_link": "http://",
                "event_link": "http://",
                "image_link": "http://",
                "start_time": "9.00",
                "end_time": "21.03.2022",
                "date": "20.03.2022",
                "is_reg_completed": False,
                "is_event_completed": False,
                "points": [
                    {
                        "point": 20.0,
                        "position": 1,
                        "department": "archi",
                    },
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
