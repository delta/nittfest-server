"""
Schemas for the API.
"""

from server.schemas.domains import Domains
from server.schemas.preferences import Preferences
from server.schemas.questions import Answer, Questions
from server.schemas.users import Users

models = [Users, Questions, Domains, Preferences, Answer]
