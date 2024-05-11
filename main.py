
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

import models
from database import engine, SessionLocal,Base
from sqlalchemy.orm import Session
from router import exercise, topic, code
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(exercise.router)
app.include_router(code.router)
app.include_router(topic.router)

