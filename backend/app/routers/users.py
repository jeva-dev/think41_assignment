from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db


router = APIRouter(
    prefix = "/users",
    tags= ["Users"]
)

@router.get('/', response_model= List[schemas.UserOut])
def getPosts(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
