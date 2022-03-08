"""
Schema for departments
"""

from sqlalchemy import Column, Integer, String

from config.database import Base


class Department(Base):
    """Department Schema"""

    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(3000))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """Representation of the object"""
        return f"<name: '{self.name}',description: '{self.description}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
