"""
Schema for Nerdle
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from config.database import Base


class Nerdle(Base):
    """Nerdle Schema"""

    __tablename__ = "nerdle"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    current_word = Column(String(100))
    score = Column(Integer)
    streak = Column(Integer)

    def __init__(self, user_id, current_word, score, streak):
        self.user_id = user_id
        self.current_word = current_word
        self.score = score
        self.streak = streak

    def __repr__(self):
        """Representation of the object"""
        return f"""<user_id: '{self.user_id}',current_word: '{self.current_word}',
                score: '{self.score}',streak: {self.streak}>"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "current_word": self.current_word,
            "score": self.score,
            "streak": self.streak,
        }
