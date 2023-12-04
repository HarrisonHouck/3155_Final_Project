from pydantic import BaseModel

class RatingBase(BaseModel):
    pizza_id: int
    rating: float

class RatingCreate(RatingBase):
    pass

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
