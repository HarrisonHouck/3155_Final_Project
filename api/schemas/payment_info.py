from pydantic import BaseModel
from datetime import datetime

class PaymentInfoBase(BaseModel):
    card_number: str
    expiration_date: str
    cvv: str

class PaymentInfoCreate(PaymentInfoBase):
    pass

class PaymentInfoUpdate(PaymentInfoBase):
    pass

class PaymentInfo(PaymentInfoBase):
    id: int
