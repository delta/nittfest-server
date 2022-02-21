"""
Schema for domains.
"""

from sqlalchemy import Column, Integer, String

from config.database import Base


class Domains(Base):
    """Domains Schema"""

    __tablename__ = "domains"
    id = Column(Integer, primary_key=True)
    domain = Column(String(20))
    description = Column(String(3000))

    def __init__(self, domain, description):
        self.domain = domain
        self.description = description

    def __repr__(self):
        """Representation of the object"""
        return f"""<domain: '{self.domain}', description: '{self.description},
        '>"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "domain": self.domain,
            "description": self.description,
        }
