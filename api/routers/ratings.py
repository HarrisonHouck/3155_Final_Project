from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import ratings as controller
from ..schemas.ratings import RatingCreate, RatingUpdate, Rating
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Ratings'],
    prefix="/ratings"
)

@router.post("/", response_model=Rating)
def add_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return controller.create_rating(db=db, rating=rating)

@router.get("/", response_model=list[Rating])
def read_all_ratings(db: Session = Depends(get_db)):
    return controller.read_all_ratings(db)

@router.get("/{rating_id}", response_model=Rating)
def read_one_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = controller.read_one_rating(db, rating_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@router.put("/{rating_id}", response_model=Rating)
def update_rating(rating_id: int, rating: RatingUpdate, db: Session = Depends(get_db)):
    updated_rating = controller.update_rating(db, rating_id, rating)
    if updated_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return updated_rating

@router.delete("/{rating_id}", response_model=Rating)
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    deleted_rating = controller.delete_rating(db, rating_id)
    if deleted_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return deleted_rating
