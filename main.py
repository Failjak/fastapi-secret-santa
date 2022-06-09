from fastapi import FastAPI, status, Query

from schemas import *
from database.base import Base
from database.session import engine

app = FastAPI()


def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


users = []


@app.get("/players", response_model=List[str])
def get_players():
    """Get all players"""
    return users


@app.get("/player")
def get_player(id: str = Query(None, min_length=1, max_length=5)):
    return users[int(id)] if len(users) >= int(id) else None


@app.post("/add_player", status_code=status.HTTP_201_CREATED)
async def post_player(*, player: Player):
    """Add new player to your game"""
    return "Hello, world!"
