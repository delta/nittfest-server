"""
Tests for scores route
"""
from fastapi.testclient import TestClient

ROUTE = "/scores"
res = [
    {
        "department": "MME",
        "total_points": 34,
        "cluster_points": [
            {"cluster": "Arts", "points": 15},
            {"cluster": "Gaming", "points": 19},
        ],
    },
    {
        "department": "EEE",
        "total_points": 33,
        "cluster_points": [
            {"cluster": "Arts", "points": 19},
            {"cluster": "Gaming", "points": 14},
        ],
    },
    {
        "department": "ICE",
        "total_points": 38,
        "cluster_points": [
            {"cluster": "Arts", "points": 20},
            {"cluster": "Gaming", "points": 18},
        ],
    },
]


def get_scores(client: TestClient):
    """
    get list of scores
    """
    get_response = client.get(url=ROUTE)
    assert get_response.status_code == 200
    assert get_response.json() == res
