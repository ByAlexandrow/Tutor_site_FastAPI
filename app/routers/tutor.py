from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .. import crud, models, schemas
from app.database import get_db


router = APIRouter()


@router.post("/", response_model=schemas.Tutor)
async def create_tutor(tutor: schemas.TutorCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_tutor(db=db, tutor=tutor)


@router.get("/", response_model=list[schemas.Tutor])
async def read_all_tutors(skip: int = 0, limit: int = 1, db: AsyncSession = Depends(get_db)):
    tutors = await crud.get_all_tutors(db, skip=skip, limit=limit)
    return tutors


@router.get("/{tutor_id}", response_model=schemas.Tutor)
async def read_tutor(tutor_id: int, db: AsyncSession = Depends(get_db)):
    db_tutor = await crud.get_tutor(db, tutor_id=tutor_id)
    if db_tutor is None:
        raise HTTPException(status_code=404, detail="Tutor is not found!")
    return db_tutor
