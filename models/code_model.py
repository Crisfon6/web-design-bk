from sqlalchemy import  Column, ForeignKey, Integer, String, DateTime
from database import Base

class Code(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    language = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    exercise = Column(Integer, ForeignKey("exercises.id"))