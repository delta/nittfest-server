"""
Schemas for the API.
"""

from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.domains import Domains
from server.schemas.event import Event
from server.schemas.point import Point
from server.schemas.preferences import Preferences
from server.schemas.questions import Answer, Questions
from server.schemas.users import Users
from server.schemas.tshirt import Tshirt

schemas = [
    Users.metadata,
]

models = [
    Domains.metadata,
    Preferences.metadata,
    Questions.metadata,
    Answer.metadata,
    Cluster.metadata,
    Event.metadata,
    Department.metadata,
    Point.metadata,
    Tshirt.metadata,
]
