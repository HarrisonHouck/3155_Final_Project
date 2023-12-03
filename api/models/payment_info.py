from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from ..models.customers import Customer  # Import the Customer model

class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))  # Reference the 'customers' table
    payment_method = Column(String(50), index=True)
    card_number = Column(String(50), index=True)
    expiration_date = Column(DateTime, nullable=False, default=datetime.now())

    # Define the relationship with the Customer model
    customer = relationship("Customer", back_populates="payment_info")
