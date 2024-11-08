from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {'description': 'Not Found'}}
)

@router.post("/")
async def sign_in():
    pass

@router.post("/sign_up")
async def sign_up():
    return 

@router.post("/{user_id}")
def sign_out(user_id):
    return 

@router.delete("/{user_id}")
def delete_user(user_id):
    return 

