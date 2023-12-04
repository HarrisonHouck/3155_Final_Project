
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    phone = Column(String(50), index=True)

    # Specify the foreign key to the payment_info relationship
    payment_info = relationship("PaymentInfo", back_populates="customer")