"""
Schema for guesses
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from config.database import Base


class Guesses(Base):
    """Guess Schema"""

    __tablename__ = "guesses"
    id = Column(Integer, primary_key=True)
    guess = Column(String(5))
    position = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __init__(self, guess, position, user_id):
        self.guess = guess
        self.position = position
        self.user_id = user_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<guess: '{self.guess}',position: '{self.position},user_id: '{self.user_id}
        >"""
