from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# This is the foundational class for a sandwich, which includes the following fields
class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    calories: Optional[int]

# Inherits from SandwichBase and is used for creating new sandwich records. This class doesn't add any new fields
class SandwichCreate(SandwichBase):
    pass

# This class is designed for updating existing sandwich records. Unlike SandwichBase, all its fields are optional, allowing for partial updates
class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None

# Represents a complete sandwich record. It inherits from SandwichBase and adds an id field
class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True
