from typing import List

from fastapi import APIRouter, Depends

from database.models import SecretSanta, SecretSantaCreate
from services.helpers.helper import get_dict_from_model
from services.mappers.player import player_model_mapper, forming_players_message
from services.tasks import send_message_to_queue_task
from services.v1.secretsanta import SecretSantaService
from services.v1.player import PlayerService

router = APIRouter(prefix='/secretsanta')


@router.get("/list", response_model=List[SecretSanta])
def get_games(service: SecretSantaService = Depends()):
    """ Getting all games """
    return service.get_list()


@router.get("/", response_model=SecretSanta)
def get_games(santa_code: int, service: SecretSantaService = Depends()):
    """ Getting game by code """
    return service.get_by_code(santa_code)


@router.post("/", response_model=SecretSanta)
def create_game(game_data: SecretSantaCreate, service: SecretSantaService = Depends()):
    """ Creating game """
    return service.create(game_data)


@router.post("/submit", response_model=SecretSanta)
def submit_game(
        santa_code: int,
        ss_service: SecretSantaService = Depends(),
        player_service: PlayerService = Depends()):
    """ Submitting the game """
    players = player_service.distribution(santa_code)
    message = forming_players_message(santa_code, players)
    send_message_to_queue_task(message)
    return ss_service.get_by_code(santa_code)
