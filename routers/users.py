from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {'description': 'Not Found'}}
)

class UserInModel(BaseModel):
    username: str
    password: str

class UserInDB(BaseModel):
    username: str
    hashed_password: str

@router.post("/sign_up")
async def sign_up(info: UserInModel):
    
    return 

@router.post("/")
async def sign_in(info: UserInModel):
    return 


class UserOut(BaseModel):
    username: str

@router.post("/{user_id}")
def sign_out(user_id):
    return 

@router.delete("/{user_id}")
def delete_user(user_id):
    return 

