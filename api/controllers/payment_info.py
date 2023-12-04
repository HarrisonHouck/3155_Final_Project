from sqlalchemy.orm import Session
from ..models.payment_info import PaymentInfo as ModelPaymentInfo
from ..schemas.payment_info import PaymentInfoCreate, PaymentInfoUpdate

def create_payment_info(db: Session, payment_info: PaymentInfoCreate):
    db_payment_info = ModelPaymentInfo(**payment_info.dict())
    db.add(db_payment_info)
    db.commit()
    db.refresh(db_payment_info)
    return db_payment_info


def read_all_payment_info(db: Session):
    return db.query(ModelPaymentInfo).all()

def read_one_payment_info(db: Session, payment_info_id: int):
    return db.query(ModelPaymentInfo).filter(ModelPaymentInfo.id == payment_info_id).first()

def update_payment_info(db: Session, payment_info_id: int, payment_info: PaymentInfoUpdate):
    db_payment_info = db.query(ModelPaymentInfo).filter(ModelPaymentInfo.id == payment_info_id).first()
    if db_payment_info:
        for key, value in payment_info.dict(exclude_unset=True).items():
            setattr(db_payment_info, key, value)
        db.commit()
        db.refresh(db_payment_info)
    return db_payment_info

def delete_payment_info(db: Session, payment_info_id: int):
    db_payment_info = db.query(ModelPaymentInfo).filter(ModelPaymentInfo.id == payment_info_id).first()
    if db_payment_info:
        db.delete(db_payment_info)
        db.commit()
        return db_payment_info
    return None
