from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import payment_info as controller
from ..schemas.payment_info import PaymentInfoCreate, PaymentInfoUpdate, PaymentInfo
from ..dependencies.database import get_db

router = APIRouter(
    tags=['PaymentInfo'],
    prefix="/payment_info"
)

@router.post("/", response_model=PaymentInfo)
def create_payment_info(payment_info: PaymentInfoCreate, db: Session = Depends(get_db)):
    return controller.create_payment_info(db=db, payment_info=payment_info)

@router.get("/", response_model=list[PaymentInfo])
def read_all_payment_info(db: Session = Depends(get_db)):
    return controller.read_all_payment_info(db)

@router.get("/{payment_info_id}", response_model=PaymentInfo)
def read_one_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    payment_info = controller.read_one_payment_info(db, payment_info_id)
    if payment_info is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return payment_info

@router.put("/{payment_info_id}", response_model=PaymentInfo)
def update_payment_info(payment_info_id: int, payment_info: PaymentInfoUpdate, db: Session = Depends(get_db)):
    updated_payment_info = controller.update_payment_info(db, payment_info_id, payment_info)
    if updated_payment_info is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return updated_payment_info

@router.delete("/{payment_info_id}", response_model=PaymentInfo)
def delete_payment_info(payment_info_id: int, db: Session = Depends(get_db)):
    deleted_payment_info = controller.delete_payment_info(db, payment_info_id)
    if deleted_payment_info is None:
        raise HTTPException(status_code=404, detail="Payment Info not found")
    return deleted_payment_info
