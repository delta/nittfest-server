"""User Model"""
from sqlalchemy import Column, Integer, String
from server.config.database import Base


class Users(Base):
    """User Model Class"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    mobile_number = Column(String)
    gender = Column(String)
