from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .. import crud, models, schemas
from app.database import get_db


router = APIRouter()

@router.post("/", response_model=schemas.PriceListCreate)
async def create_pricelist(pricelist: schemas.PriceListCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_pricelist(db=db, pricelist=pricelist)


@router.get("/", response_model=list[schemas.PriceList])
async def read_pricelists(skip: int = 0, limit: int = 1, db: AsyncSession = Depends(get_db)):
    pricelists = await crud.get_all_prices(db, skip=skip, limit=limit)
    return pricelists


@router.get("/{pricelist_id}", response_model=schemas.PriceList)
async def read_pricelist(pricelist_id: int, db: AsyncSession = Depends(get_db)):
    db_pricelist = await crud.get_pricelist(db, pricelist_id=pricelist_id)
    if db_pricelist is None:
        raise HTTPException(status_code=404, detail='Price in not found!')
    return db_pricelist
