from fastapi import FastAPI

from endpoints import users, courses, sections
from data_base.db_setup import engine
from data_base.db_models import user, course

user.Base.metadata.create_all(bind = engine)
course.Base.metadata.create_all(bind = engine)

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
