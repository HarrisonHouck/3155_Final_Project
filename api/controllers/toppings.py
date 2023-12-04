from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import toppings as model
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from datetime import datetime
from ..models.toppings import Topping
from ..models.orders import Order
from ..models.pizzas import Pizza, pizza_topping_association


def read_all(db: Session):
    try:
        result = db.query(model.Topping).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Topping).filter(model.Topping.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def get_most_popular_topping(db: Session, start_date: datetime, end_date: datetime):
    # Join the necessary tables
    subquery = db.query(Topping.name, func.count(Topping.id).label('topping_count')).join(
        pizza_topping_association).join(Pizza).join(Order).filter(
        Order.order_date >= start_date, Order.order_date <= end_date).group_by(Topping.name).subquery()

    # Get the most popular topping by counting occurrences
    result = db.query(subquery.c.name).order_by(subquery.c.topping_count.desc()).first()
    return result