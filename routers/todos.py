from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {'description': 'Not Found'}}
)

@router.get("/")
async def read_todos():
    return 

@router.post("/")
async def add_todo():
    return 

class Todo(BaseModel):
    todo: str
    is_completed: bool = False


@router.put("/{todo_id}")
async def update_todo(todo_id):
    return 

@router.delete("/{todo_id}")
async def delete_todo(todo_id):
    return 

@router.patch("/{todo_id}")
async def switch_todo(todo_id):
    return
