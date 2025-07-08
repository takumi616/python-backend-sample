from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Vocabulary(Base):
    __tablename__ = "vocabularies"

    vocabulary_no = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    meaning = Column(Text, nullable=False)
    sentence = Column(Text, nullable=False)
