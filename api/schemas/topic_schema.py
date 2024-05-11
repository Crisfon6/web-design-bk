from pydantic import BaseModel
from typing import List
from .exercise_schema import ExerciseBase

class TopicBase(BaseModel):
    title: str
    description: str
    exercises: List[ExerciseBase]