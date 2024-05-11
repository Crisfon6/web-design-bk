from pydantic import BaseModel
import datetime

class CodeBase(BaseModel):
    code: str
    description: str
    language: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exercise: int