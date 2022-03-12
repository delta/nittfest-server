"""
T-shirt Registration Schema
"""
from sqlalchemy import Column, ForeignKey, Integer, Enum

from config.database import Base


class Tshirt(Base):
    """T-shirt Registration Schema"""

    __tablename__ = "tshirts"
    id = Column(Integer, primary_key=True)
    size = Column(Enum("S", "M", "L", "XL", "XXL"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __init__(self, size, user_id):
        self.size = size
        self.user_id = user_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<size: '{self.size}', user_id: '{self.user_id}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "size": self.size,
            "user_id": self.user_id,
        }
