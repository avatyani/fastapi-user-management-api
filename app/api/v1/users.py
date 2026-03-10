from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserResponse
from app.controllers import user_controller

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    return user_controller.create_user(user)