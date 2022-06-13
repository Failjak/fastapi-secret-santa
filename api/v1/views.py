from typing import List

from fastapi import APIRouter, Query, status

from schemas import Player

router = APIRouter(prefix='/v1')


@router.get("/players", response_model=List[str])
def get_players():
    """Get all players"""
    return ["Players"]


@router.get("/player")
def get_player(id: str = Query(None, min_length=1, max_length=5)):
    return "Returned user by id"


@router.post("/add_player", status_code=status.HTTP_201_CREATED)
async def post_player(*, player: Player):
    """Add new player to your game"""
    return "Hello, world!"
