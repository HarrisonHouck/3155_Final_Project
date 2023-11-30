from typing import Optional
from pydantic import BaseModel
#  This is the foundational class for a sandwich tag
class SandwichTagBase(BaseModel):
    tags: str
# Inherits from SandwichTagBase and is used for creating new sandwich tag records. It adds an additional field
class SandwichTagCreate(SandwichTagBase):
    sandwich_id: int
    tags: str

# Designed for updating existing sandwich tags. All fields are optional, enabling partial updates
class SandwichTagUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    tags: Optional[str] = None

#This class represents a complete sandwich tag record. It simply inherits from SandwichTagBase without adding new fields
class SandwichTag(SandwichTagBase):
    pass

    class ConfigDict:
        from_attributes = True
