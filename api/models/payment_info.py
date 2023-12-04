from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String(16), index=True)
    expiration_date = Column(String(7), index=True)
    cvv = Column(String(3), index=True)
