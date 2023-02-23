from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title = "Learning Management System",
    description = "System for managing students and courses.",
    version = "0.0.1",
    contact = {
        "name": "Amir",
        "email": "amir@example.com",
    },
    license_info = {
        "name": "MIT",
    }
)

list_of_users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model = List[User])
async def get_all_users():
    return list_of_users


@app.post("/user")
async def create_new_user(user: User):
    list_of_users.append(user)
    return "The user is successfully added."


@app.get("/users/{id}")
async def get_user_by_index(
    id: int = Path(..., description = "The ID of a user you want to retrieve.", gt = 2),
    q: str = Query(None, max_length = 5)
    ):
    return {"user": list_of_users[id], "query": q}
