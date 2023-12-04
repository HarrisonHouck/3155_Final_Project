from pydantic import BaseModel
from datetime import datetime

class PromotionBase(BaseModel):
    name: str
    discount_rate: float
    active: bool
    start_date: datetime
    end_date: datetime

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
