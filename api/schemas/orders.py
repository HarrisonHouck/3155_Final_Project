from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail

# This is the foundational class for representing an order. It includes several fields:
class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    phone_number: Optional[int]
    address: str
    type: str
    status: str = "Not Started"

#  Inherits from OrderBase and is used for creating new orders.
class OrderCreate(OrderBase):
    pass

# This class is used for updating existing orders. Unlike OrderBase, all its fields are optional.
class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    phone_number: Optional[int]
    address: Optional[str]
    type: Optional[str]
    status: Optional[str] = "In Progress"

# This class represents a complete order and includes fields from OrderBase along with additional ones
class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
