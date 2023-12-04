from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CrustBase(BaseModel):
    name: str
    price: float


class Crust(CrustBase):
    id: int

    class ConfigDict:
        from_attributes = True
