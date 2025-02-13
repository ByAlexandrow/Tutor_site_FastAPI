from pydantic import BaseModel


class TutorBase(BaseModel):
    title: str
    description: str


class TutorCreate(TutorBase):
    pass


class Tutor(TutorBase):
    id: int

    class Config:
        orm_mode = True


class PriceListBase(BaseModel):
    pricelist_title: str
    pricelist_description: str
    price: int


class PriceListCreate(PriceListBase):
    pass


class PriceList(PriceListBase):
    id: int

    class Config:
        orm_mode = True
