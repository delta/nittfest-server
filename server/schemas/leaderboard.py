"""
Schema for point
"""

from sqlalchemy import Column, Float, ForeignKey, Integer

from config.database import Base


class Leaderboard(Base):
    """Leaderboard Schema"""

    __tablename__ = "leaderboard"
    id = Column(Integer, primary_key=True)
    point = Column(Float, nullable=False)
    department_id = Column(
        Integer, ForeignKey("departments.id"), nullable=True
    )

    def __init__(self, point, department_id):
        self.point = point
        self.department_id = department_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<point: '{self.point}',department_id: '{self.department_id}'>"""
