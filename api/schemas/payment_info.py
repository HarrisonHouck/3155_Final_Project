from pydantic import BaseModel

class PaymentInfoBase(BaseModel):
    customer_id: int
    card_number: str
    expiration_date: str
    cvv: str

class PaymentInfoCreate(PaymentInfoBase):
    pass

class PaymentInfoUpdate(PaymentInfoBase):
    pass

class PaymentInfo(PaymentInfoBase):
    id: int
