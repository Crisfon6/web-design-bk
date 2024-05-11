from pydantic import BaseModel

class ExerciseBase(BaseModel):
    title: str
    description: str