from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from models.code_model  import Code
from database import SessionLocal, engine
from schemas.code_schema import CodeBase
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/codes/")
async def create_code(code: CodeBase, db: db_dependency):
    db_code = Code(code=code.code, description=code.description, language=code.language, created_at=code.created_at, updated_at=code.updated_at, exercise=code.exercise)
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return code

# create crud
@router.get("/codes/", response_model=List[CodeBase])
async def read_codes(db: db_dependency):
    codes = db.query(Code).all()
    return codes

@router.get("/code/{code_id}", response_model=CodeBase)
async def read_code(code_id: int, db: db_dependency):
    code = db.query(Code).filter(Code.id == code_id).first()
    if code is None:
        raise HTTPException(status_code=404, detail="Code not found")
    return code

@router.put("/code/{code_id}")
async def update_code(code_id: int, code: CodeBase, db: db_dependency):
    db_code = db.query(Code).filter(Code.id == code_id).first()
    if db_code is None:
        raise HTTPException(status_code=404, detail="Code not found")
    db_code.code = code.code
    db_code.description = code.description
    db_code.language = code.language
    db_code.created_at = code.created_at
    db_code.updated_at = code.updated_at
    db_code.exercise = code.exercise
    db.commit()
    db.refresh(db_code)
    return code

@router.delete("/code/{code_id}")
async def delete_code(code_id: int, db: db_dependency):
    code = db.query(Code).filter(Code.id == code_id).first()
    if code is None:
        raise HTTPException(status_code=404, detail="Code not found")
    db.delete(code)
    db.commit()
    return {"message": "Code deleted"}

# Path: router/exercise.py