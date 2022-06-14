from typing import List

from fastapi import APIRouter, Query, status

from database.session import SessionLocal
from database.schemas import CardSerializer, SecretSantaSerializer, PlayerSerializer
from database.models import Card, SecretSanta, Player

router = APIRouter(prefix='/v1')


@router.get("/game", response_model=List[SecretSantaSerializer])
def get_game():
    session = SessionLocal()
    games = (
        session
        .query(SecretSanta)
        .all()
    )

    return games


# @router.get("/game")
# def get_player(id: str = Query(None, min_length=1, max_length=5)):
#     return "Returned user by id"


@router.post("/game", status_code=status.HTTP_201_CREATED)
async def post_game(*, game: SecretSantaSerializer):
    return "Hello, world!"
