from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import user as user_controller
from app.schemas import user as user_schema
from typing import List

router = APIRouter()

@router.post("/users/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)

@router.get("/users/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_controller.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=List[user_schema.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)
