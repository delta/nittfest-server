"""
Users Schema
"""

from sqlalchemy import Column, Integer, String, ForeignKey

from config.database import Base


class Users(Base):
    """Users Models"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    mobile_number = Column(String(255))
    gender = Column(String(255))
    department_id = Column(Integer, ForeignKey("departments.id"))

    def __init__(self, name, email, mobile_number, gender, department_id):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.gender = gender
        self.department_id = department_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<name: '{self.name}', email: '{self.email}',
        mobile: '{self.mobile_number}', gender: '{self.gender}',
        department_id: '{self.department_id}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile_number,
            "gender": self.gender,
            "department_id": self.department_id,
        }
