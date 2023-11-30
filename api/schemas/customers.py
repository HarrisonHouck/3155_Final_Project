from typing import Optional
from pydantic import BaseModel

# This is the base class for representing a customer.
class CustomerBase(BaseModel):
    customer_name: str
    phone_number: Optional[int]
    address: str
    payment_info: str

#  This class inherits from CustomerBase and doesn't add any additional fields. It's typically used for creating new customer records.
class CustomerCreate(CustomerBase):
    pass

# This class is for updating an existing customer's information.
class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_number: Optional[int]
    address: Optional[str]
    payment_info: Optional[str]

# This class also inherits from CustomerBase but adds an id field. 
class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True
