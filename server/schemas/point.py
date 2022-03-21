"""
Schema for point
"""

from sqlalchemy import Column, Float, ForeignKey, Integer

from config.database import Base


class Point(Base):
    """Point Schema"""

    __tablename__ = "points"
    id = Column(Integer, primary_key=True)
    point = Column(Float, nullable=False)
    position = Column(Integer, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    department_id = Column(
        Integer, ForeignKey("departments.id"), nullable=True
    )

    def __init__(self, point, position, event_id, department_id):
        self.point = point
        self.position = position
        self.event_id = event_id
        self.department_id = department_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<point: '{self.point}',position: '{self.position},event_id: '{self.event_id}
        ,department_id: '{self.department_id}'>"""
