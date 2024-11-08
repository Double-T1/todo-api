from fastapi import APIRouter

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {'description': 'Not Found'}}
)

@router.get("/")
async def get_todo():
    return 

@router.post("/")
async def add_todo():
    return 

@router.put("/{todo_id}")
async def update_todo(todo_id):
    return 

@router.delete("/{todo_id}")
async def delete_todo(todo_id):
    return 

@router.patch("/{todo_id}")
async def switch_todo(todo_id):
    return
