from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Crust(Base):
    __tablename__ = "crusts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, primary_key=True, index=True, autoincrement=True)
    price = Column(Integer, index=True, nullable=False)
    
    pizza_id = Column(Integer, ForeignKey("pizzas.id"))
    pizza = relationship("Pizza", back_populates="crusts")
