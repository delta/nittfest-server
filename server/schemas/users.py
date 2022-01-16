"""
Users Schema
"""

from sqlalchemy import Column, Integer, String

from server.config.database import Base


class Users(Base):
    """Users Models"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    mobile_number = Column(String(255))
    gender = Column(String(255))

    def __init__(self, name, email, mobile_number, gender):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.gender = gender

    def __repr__(self):
        """Representation of the object"""
        return """<Name: '{self.name}', Email: '{self.email}',
        Mobile: '{self.mobile_number}', Gender: '{self.gender}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile_number,
            "gender": self.gender,
        }
