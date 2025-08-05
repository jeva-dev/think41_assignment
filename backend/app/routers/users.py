from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db


router = APIRouter(
    prefix = "/users",
    tags= ["Users"]
)

@router.get('/', response_model= List[schemas.UserOut])
def getUser(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# @router.get("/{id}", response_model= schemas.UserOut)
# def one_customer(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found")
#     return user


@router.get("/users/{user_id}", response_model=schemas.UserWithOrderCount)
def get_user_with_order_count(user_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(
            models.User,
            func.count(models.Order.order_id).label("order_count")
        )
        .outerjoin(models.Order, models.User.id == models.Order.user_id)
        .filter(models.User.id == user_id)
        .group_by(models.User.id)
        .first()
    )

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    user, order_count = result
    user.order_count = order_count
    return user