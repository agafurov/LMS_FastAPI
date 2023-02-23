from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from endpoints import users, courses, sections

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

app.include_router(router = users.router)
app.include_router(router = courses.router)
app.include_router(router = sections.router)
