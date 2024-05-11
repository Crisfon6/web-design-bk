from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from models.topic_model  import Topic
from database import SessionLocal, engine
from schemas.topic_schema import TopicBase
from sqlalchemy.orm import Session



router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]

#create crud to topic
@router.post("/topics/")
async def create_topic(topic: TopicBase, db: db_dependency):
    db_topic = Topic(title=topic.title, description=topic.description)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return topic

@router.get("/topics/", response_model=List[TopicBase])
async def read_topics(db: db_dependency):
    topics = db.query(Topic).all()
    return topics

@router.get("/topic/{topic_id}", response_model=TopicBase)
async def read_topic(topic_id: int, db: db_dependency):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic

@router.put("/topic/{topic_id}")
async def update_topic(topic_id: int, topic: TopicBase, db: db_dependency):
    db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    db_topic.title = topic.title
    db_topic.description = topic.description
    db.commit()
    db.refresh(db_topic)
    return topic

@router.delete("/topic/{topic_id}")
async def delete_topic(topic_id: int, db: db_dependency):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    db.delete(topic)
    db.commit()
    return {"message": "Topic deleted"}

