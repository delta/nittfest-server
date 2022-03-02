"""
Schemas for the API.
"""

from server.schemas.domains import Domains
from server.schemas.preferences import Preferences
from server.schemas.questions import Answer, Questions
from server.schemas.users import Users
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point

models = [
    Users,
    Questions,
    Domains,
    Preferences,
    Answer,
    Cluster,
    Event,
    Department,
    Point,
]
