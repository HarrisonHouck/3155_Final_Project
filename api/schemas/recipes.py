from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich

# This is the foundational class for a recipe. It includes a single field
amount
class RecipeBase(BaseModel):
    amount: int

#  Inherits from RecipeBase and is used for creating new recipes. It adds two fields to specify the IDs of the sandwich and the resource
class RecipeCreate(RecipeBase):
    sandwich_id: int
    resource_id: int
    
# Designed for updating existing recipes. All fields are optional to allow for partial updates:
class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None
    
# Represents a complete recipe. It inherits from RecipeBase and includes additional fields:
class Recipe(RecipeBase):
    id: int
    sandwich: Sandwich = None
    resource: Resource = None

    class ConfigDict:
        from_attributes = True
