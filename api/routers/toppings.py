from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import toppings as controller
from ..schemas import toppings as schema
from ..dependencies.database import engine, get_db
from datetime import datetime

router = APIRouter(
    tags=['Toppings'],
    prefix="/toppings"
)


@router.get("/", response_model=list[schema.Topping])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Topping)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.get("/popular-topping/")
def read_most_popular_topping(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    most_popular_topping = controller.get_most_popular_topping(db, start_date, end_date)
    return most_popular_topping