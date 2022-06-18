from typing import List

from fastapi import APIRouter, Depends

from database.models import SecretSanta, SecretSantaCreate
from services.v1.secretsanta import SecretSantaService

router = APIRouter(prefix='/secretsanta')


@router.get("/list", response_model=List[SecretSanta])
def get_games(service: SecretSantaService = Depends()):
    return service.get_list()


@router.post("/", response_model=SecretSanta)
def create_game(game_data: SecretSantaCreate, service: SecretSantaService = Depends()):
    return service.create(game_data)

# @router.get("/game")
# def get_player(id: str = Query(None, min_length=1, max_length=5)):
#     return "Returned user by id"


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_game(*, game: SecretSantaSerializer):
#     return "Hello, world!"
