from fastapi import FastAPI, Body, Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


from db.db import get_db
from models.models import Crypto
from par import insert_value

app = FastAPI(title="CRYPTO")
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
def read_items(request: Request, db: Session = Depends(get_db)):
    insert_value()
    items = db.query(Crypto).all()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})


@app.get("/test", response_class=HTMLResponse)
def read_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": "items"})
