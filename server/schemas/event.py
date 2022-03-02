"""
Schema for event
"""


from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from config.database import Base


class Event(Base):
    """Event Schema"""

    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(3000))
    cluster_id = Column(Integer, ForeignKey("clusters.id"), nullable=False)
    rules = Column(String(3000))
    form_link = Column(String(255))
    event_link = Column(String(255))
    image_link = Column(String(255))
    start_time = Column(String(25))
    end_time = Column(String(25))
    date = Column(String(25))
    is_reg_completed = Column(Boolean, default=False)
    is_event_completed = Column(Boolean, default=False)

    def __init__(
        self,
        name,
        description,
        cluster_id,
        rules,
        form_link,
        event_link,
        image_link,
        start_time,
        end_time,
        date,
        is_reg_completed,
        is_event_completed,
    ):
        self.name = name
        self.description = description
        self.cluster_id = cluster_id
        self.rules = rules
        self.form_link = form_link
        self.event_link = event_link
        self.image_link = image_link
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.is_reg_completed = is_reg_completed
        self.is_event_completed = is_event_completed

    def __repr__(self):
        """Representation of the object"""
        return f"""<name: '{self.name}',
        description: '{self.description},
        cluster_id: '{self.cluster_id}',
        rules: '{self.rules}',
        is_reg_completed = '{self.is_reg_completed}',
        form_link: '{self.form_link}',
        event_link: '{self.event_link}',
        image_link: '{self.image_link}',
        start_time: '{self.start_time}',
        end_time: '{self.end_time}',
        date: '{self.date}',
        is_event_completed '{self.is_event_completed}',>"""
