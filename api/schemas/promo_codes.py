from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# This is the foundational class for representing a promo code
class PromoCodeBase(BaseModel):
    discount: float
    description: str
    end_date: datetime

# Inherits from PromoCodeBase without adding any new fields. It's used specifically for creating new promo codes, ensuring that all the base fields are provided.
class PromoCodeCreate(PromoCodeBase):
    pass

# This class is intended for updating existing promo codes. Different from PromoCodeBase, its fields are optional
class PromoCodeUpdate(BaseModel):
    discount: Optional[float]
    description: Optional[str]
    end_date: Optional[datetime]

# This class represents a complete promo code, inheriting from PromoCodeBase 
class PromoCode(PromoCodeBase):
    code: str
    start_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
