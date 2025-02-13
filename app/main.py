from fastapi import FastAPI, Request, Depends

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base, get_db
from app.routers import tutor, pricelist

from . import crud


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


app.include_router(tutor.router, prefix="/tutors", tags=["tutors"])
app.include_router(pricelist.router, prefix="/pricelist", tags=["pricelist"])


@app.get("/", response_class=HTMLResponse, name='homepage:index')
async def read_tutors_template(request: Request, db=Depends(get_db)):
    tutors = await crud.get_all_tutors(db)
    pricelist = await crud.get_all_prices(db)
    return templates.TemplateResponse("homepage/index.html", {"request": request, "tutors": tutors, "pricelist": pricelist})
