from typing import List

from fastapi import APIRouter, HTTPException, status

from app.schemas.user import User
from app.services.user_service import list_users, get_user

router = APIRouter(tags=["users"])


@router.get("/users", response_model=List[User])
def list_users_endpoint():
    return list_users()


@router.get("/users/{user_id}", response_model=User)
def get_user_endpoint(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user
