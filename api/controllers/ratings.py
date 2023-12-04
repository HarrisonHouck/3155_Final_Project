from sqlalchemy.orm import Session
from ..models.ratings import Rating as ModelRating
from ..schemas.ratings import RatingCreate, RatingUpdate

def create_rating(db: Session, rating: RatingCreate):
    db_rating = ModelRating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def read_all_ratings(db: Session):
    return db.query(ModelRating).all()

def read_one_rating(db: Session, rating_id: int):
    return db.query(ModelRating).filter(ModelRating.id == rating_id).first()

def update_rating(db: Session, rating_id: int, rating: RatingUpdate):
    db_rating = db.query(ModelRating).filter(ModelRating.id == rating_id).first()
    if db_rating:
        for key, value in rating.dict(exclude_unset=True).items():
            setattr(db_rating, key, value)
        db.commit()
        db.refresh(db_rating)
    return db_rating

def delete_rating(db: Session, rating_id: int):
    db_rating = db.query(ModelRating).filter(ModelRating.id == rating_id).first()
    if db_rating:
        db.delete(db_rating)
        db.commit()
        return db_rating
    return None
