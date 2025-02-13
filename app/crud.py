from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas


async def get_tutor(db: AsyncSession, tutor_id: int):
    result = await db.execute(select(models.Tutor).filter(models.Tutor.id == tutor_id))
    return result.scalars().first()


async def get_all_tutors(db: AsyncSession, skip: int = 0, limit: int = 1):
    result = await db.execute(select(models.Tutor).offset(skip).limit(limit))
    return result.scalars().all()


async def create_tutor(db: AsyncSession, tutor: schemas.TutorCreate):
    db_tutor = models.Tutor(title=tutor.title, description=tutor.description)
    db.add(db_tutor)
    await db.commit()
    await db.refresh(db_tutor)
    return db_tutor


async def get_pricelist(db: AsyncSession, pricelist_id: int):
    result = await db.execute(select(models.PriceList).filter(models.PriceList.id == pricelist_id))
    return result.scalars().first()


async def get_all_prices(db: AsyncSession, skip: int = 0, limit: int = 1):
    result = await db.execute(select(models.PriceList).offset(skip).limit(limit))
    return result.scalars().all()


async def create_pricelist(db: AsyncSession, pricelist: schemas.PriceListCreate):
    db_pricelist = models.PriceList(
        pricelist_title=pricelist.pricelist_title,
        pricelist_description=pricelist.pricelist_description,
        price=pricelist.price
    )
    db.add(db_pricelist)
    await db.commit()
    await db.refresh(db_pricelist)
    return db_pricelist
