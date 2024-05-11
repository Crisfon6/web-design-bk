from sqlalchemy import  Column, ForeignKey, Integer, String, DateTime
from database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    topic = Column(Integer, ForeignKey("topics.id"))