from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from models.exercise_model  import Exercise
from database import SessionLocal, engine
from schemas.exercise_schema import ExerciseBase
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/exercises/", response_model=List[ExerciseBase])
async def read_exercises(db: db_dependency):
    exercises = db.query(Exercise).all()
    return exercises

@router.get("/exercise/{exercise_id}", response_model=ExerciseBase)
async def read_exercise(exercise_id: int, db: db_dependency):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

@router.post("/exercises/")
async def create_exercise(exercise: ExerciseBase, db: db_dependency):
    db_exercise = Exercise(title=exercise.title, description=exercise.description)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return exercise

@router.put("/exercise/{exercise_id}")
async def update_exercise(exercise_id: int, exercise: ExerciseBase, db: db_dependency):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    db_exercise.title = exercise.title
    db_exercise.description = exercise.description
    db.commit()
    db.refresh(db_exercise)
    return exercise

@router.delete("/exercise/{exercise_id}")
async def delete_exercise(exercise_id: int, db: db_dependency):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    db.delete(exercise)
    db.commit()
    return {"message": "Exercise deleted"}