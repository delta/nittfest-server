"""
Schema for cluster
"""


from sqlalchemy import Column, Integer, String

from config.database import Base


class Cluster(Base):
    """Cluster Schema"""

    __tablename__ = "clusters"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image_link = Column(String(255))

    def __init__(self, name, image_link):
        self.name = name
        self.image_link = image_link

    def __repr__(self):
        """Representation of the object"""
        return f"<name: '{self.name}',image_link: '{self.image_link}'>"

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link,
        }
