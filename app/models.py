from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Tutor(Base):
    __tablename__ = 'tutor_bio'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)


class PriceList(Base):
    __tablename__ = 'price_list'

    id = Column(Integer, primary_key=True)
    pricelist_title = Column(String, nullable=False)
    pricelist_description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
