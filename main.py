from fastapi import FastAPI, status

from models import *

app = FastAPI()


users = []


@app.get("/players", response_model=List[str])
def get_players():
    """Get all players"""
    return users


@app.post("/add_player", status_code=status.HTTP_201_CREATED)
async def post_player(*, player: Player):
    """Add new player to your game"""
    return "hui"
