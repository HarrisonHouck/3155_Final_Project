from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotion as controller
from ..schemas.promotion import PromotionCreate, Promotion
from ..dependencies.database import get_db

router = APIRouter(prefix="/promotions", tags=["Promotions"])

@router.post("/", response_model=Promotion)
def create_promotion(promotion: PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db=db, promotion=promotion)

@router.get("/{promotion_id}", response_model=Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = controller.get_promotion(db, promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion

@router.get("/", response_model=list[Promotion])
def read_all_promotions(db: Session = Depends(get_db)):
    return controller.get_all_promotions(db)

# Add more routes as needed
