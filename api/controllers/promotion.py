from sqlalchemy.orm import Session
from ..models.promotion import Promotion as ModelPromotion
from ..schemas.promotion import PromotionCreate

def create_promotion(db: Session, promotion: PromotionCreate):
    db_promotion = ModelPromotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def get_promotion(db: Session, promotion_id: int):
    return db.query(ModelPromotion).filter(ModelPromotion.id == promotion_id).first()

def get_all_promotions(db: Session):
    return db.query(ModelPromotion).all()

# Add more functions as needed
