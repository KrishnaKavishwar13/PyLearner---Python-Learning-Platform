from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # mcq / code
    question = Column(String)
    options = Column(JSON, nullable=True)
    correct_answer = Column(String)
    difficulty = Column(String)  # easy / medium / hard