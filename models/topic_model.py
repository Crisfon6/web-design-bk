from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)