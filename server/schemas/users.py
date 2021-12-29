"""
User Schema
"""

from sqlalchemy import Column, Integer, String

from server.config.database import Base


class User(Base):
    """User Models"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    emailid = Column(String(50), unique=True)

    def __init__(self, username, emailid):
        self.username = username
        self.emailid = emailid

    def __repr__(self):
        """Representation of the object"""
        return "<User '{self.username}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "username": self.username,
            "emailid": self.emailid,
        }
