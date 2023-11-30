from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

# This is the base class for an order detail
class OrderDetailBase(BaseModel):
    amount: int

# This class inherits from OrderDetailBase and is used specifically for creating new order details. It adds two additional fields.
class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int
    
# This class is used for updating existing order details. Unlike the create class, all fields here are optional, allowing for partial updates of an order detail.
class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None

# This class represents a complete order detail, inheriting from OrderDetailBase and adding a few fields:
class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Sandwich = None

    class ConfigDict:
        from_attributes = True
