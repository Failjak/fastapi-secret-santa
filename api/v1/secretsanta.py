from typing import List

from fastapi import APIRouter, Depends

from database.models import SecretSanta, SecretSantaCreate
from services.v1.secretsanta import SecretSantaService

router = APIRouter(prefix='/secretsanta')


@router.get("/list", response_model=List[SecretSanta])
def get_games(service: SecretSantaService = Depends()):
    """ Getting games """
    return service.get_list()


@router.post("/", response_model=SecretSanta)
def create_game(game_data: SecretSantaCreate, service: SecretSantaService = Depends()):
    """ Creating game """
    return service.create(game_data)
