from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

list_of_users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model = List[User])
async def get_all_users():
    return list_of_users


@router.post("/user")
async def create_new_user(user: User):
    list_of_users.append(user)
    return "The user is successfully added."


@router.get("/users/{id}")
async def get_user_by_index(id: int):
    return {"user": list_of_users[id]}
