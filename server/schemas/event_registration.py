"""
T-shirt Registration Schema
"""
from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class EventRegistration(Base):
    """Event Registration Schema"""

    __tablename__ = "event_registration"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<event_id: '{self.event_id}', user_id: '{self.user_id}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "event_id": self.event_id,
            "user_id": self.user_id,
        }
