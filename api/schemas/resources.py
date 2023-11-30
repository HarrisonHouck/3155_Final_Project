from datetime import datetime
from typing import Optional
from pydantic import BaseModel

#  This is the foundational class for a resource, which includes item and amount
class ResourceBase(BaseModel):
    item: str
    amount: int

# Inherits from ResourceBase and is used for creating new resource records. It doesn't add any new fields
class ResourceCreate(ResourceBase):
    pass

# Designed for updating existing resources. All its fields are optional
class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None

# Represents a complete resource entity. It inherits from ResourceBase and adds an id field:
class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
