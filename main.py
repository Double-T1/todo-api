from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from routers import users, todos

app = FastAPI()
app.include_router(users.router)
app.include_router(todos.router)

@app.get("/", tags=["home"])
async def index():
    pass


