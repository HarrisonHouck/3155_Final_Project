from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)
    rating = Column(Float, nullable=False)
    # You can also add user_id if you want to track which user rated the pizza
