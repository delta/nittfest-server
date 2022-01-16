"""
Questions Schema
"""

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import PickleType

from server.config.database import Base


class Questions(Base):
    """Questions Schema"""

    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String(2000))
    is_subjective = Column(Boolean)
    options = Column(PickleType)
    domain = Column(String(100))

    def __init__(self, question, is_subjective, options, domain):
        self.question = question
        self.is_subjective = is_subjective
        self.options = options
        self.domain = domain

    def __repr__(self):
        """Representation of the object"""
        return "<Question '{self.question}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "question": self.question,
            "is_subjective": self.is_subjective,
            "options": self.options,
            "domain": self.domain,
        }
