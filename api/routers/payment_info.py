from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.payment_info import PaymentInfoCreate, PaymentInfo, PaymentInfoUpdate
from ..controllers.payment_info import (
    create_payment_info,
    read_all_payment_info,
    read_one_payment_info,
    update_payment_info,
    delete_payment_info,
)
from ..dependencies.database import get_db

router = APIRouter(prefix="/payment_info", tags=["PaymentInfo"])

@router.post("/", response_model=PaymentInfo)
def create_payment_info(payment_info: PaymentInfoCreate, db: Session = Depends(get_db)):
    return create_payment_info(db, payment_info)

@router.get("/", response_model=list[PaymentInfo])
def read_all_payment_info(db: Session = Depends(get_db)):
    return read_all_payment_info(db)

@router.get("/{payment_info_id}", response_model=PaymentInfo)
def read_one_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    payment_info = read_one_payment_info(db, payment_info_id)
    if payment_info is None:
        raise HTTPException(status_code=404, detail="PaymentInfo not found")
    return payment_info

@router.put("/{payment_info_id}", response_model=PaymentInfo)
def update_payment_info(payment_info_id: int, payment_info: PaymentInfoUpdate, db: Session = Depends(get_db)):
    updated_payment_info = update_payment_info(db, payment_info_id, payment_info)
    if updated_payment_info is None:
        raise HTTPException(status_code=404, detail="PaymentInfo not found")
    return updated_payment_info

@router.delete("/{payment_info_id}", response_model=PaymentInfo)
def delete_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    deleted_payment_info = delete_payment_info(db, payment_info_id)
    if deleted_payment_info is None:
        raise HTTPException(status_code=404, detail="PaymentInfo not found")
    return deleted_payment_info
