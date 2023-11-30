from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# This is the base class for a review, containing the essential fields
class ReviewBase(BaseModel):
    rating: int
    description: Optional[str] = None
    date: Optional[datetime]

#  Inherits from ReviewBase and is used for creating new reviews. It adds an additional field
class ReviewCreate(ReviewBase):
    customer_id: int
# Designed for updating existing reviews. All its fields are optional, enabling partial updates
class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    customer_id: Optional[str] = None
# Represents a complete review. It inherits from ReviewBase and includes additional fields
class Review(ReviewBase):
    id: int
    customers: Customers = None

    class ConfigDict:
        from_attributes = True
