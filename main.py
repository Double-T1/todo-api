from fastapi import FastAPI
from routers import users, todos
from enum import Enum

app = FastAPI()
app.include_router(users.router)
app.include_router(todos.router)

@app.get("/", tags=["home"])
async def index():
    return {"hello": "world"}
    

class TeamName(str, Enum):
    celtics = "Celtics"
    knicks = "Knicks"
    sixers = "Sixers"

@app.get("/test/{team_name}", tags=["test"])
def test(team_name: TeamName):
    if team_name is TeamName.celtics:
        return {"team_name": team_name, "message": "2024 champion!!"}
    
    if team_name is TeamName.knicks:
        return {"team_name": team_name, "message": "Bunch of lunatics."}
    
    if team_name is TeamName.sixers:
        return {"team_name": team_name, "message": "Trust the process."}

    return {"message": "hehe haha"}

