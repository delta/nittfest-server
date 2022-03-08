"""
Questions Schema
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.types import PickleType

from config.database import Base


class Questions(Base):
    """Questions Schema"""

    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String(2000))
    year = Column(Integer)
    is_subjective = Column(Boolean)
    options = Column(PickleType)
    domain_id = Column(Integer, ForeignKey("domains.id"))

    def __init__(self, question, is_subjective, options, domain_id, year):
        self.question = question
        self.is_subjective = is_subjective
        self.options = options
        self.domain_id = domain_id
        self.year = year

    def __repr__(self):
        """Representation of the object"""
        return f"<Question '{self.question}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "question": self.question,
            "is_subjective": self.is_subjective,
            "options": self.options,
        }


class Answer(Base):
    """Answer Schema"""

    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    answer = Column(String(2000))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, answer, question_id, user_id):
        self.answer = answer
        self.question_id = question_id
        self.user_id = user_id

    def __repr__(self):
        """Representation of the object"""
        return f"<Answer '{self.answer}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "answer": self.answer,
            "question_id": self.question_id,
            "user_id": self.user_id,
        }
