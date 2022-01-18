"""
Schema for preferences.
"""

from sqlalchemy import Column, Integer, String, ForeignKey

from server.config.database import Base


class Preferences(Base):
    """Preference Schema"""

    __tablename__ = "preferences"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    preference_no = Column(Integer)
    domain = Column(String(100))

    def __init__(self, user_id, preference_no, domain):
        self.user_id = user_id
        self.preference_no = preference_no
        self.domain = domain

    def __repr__(self):
        """Representation of the object"""
        return f"""<user_id: '{self.user_id}', preference_no: '{self.preference_no}',
        domain: '{self.domain}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "preference_no": self.preference_no,
            "domain": self.domain,
        }
