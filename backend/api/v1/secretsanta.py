from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from database.models import SecretSanta, SecretSantaCreate
from database.schemas import StatusType
from services.mappers.player import forming_players_message
from services.tasks.tasks import send_message_to_queue_task
from services.v1.common.routes import ValidationErrorLoggingRoute
from services.v1.player import PlayerService
from services.v1.secretsanta import SecretSantaService

router = APIRouter(prefix='/secretsanta', route_class=ValidationErrorLoggingRoute)


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
    """
    Submitting the game

    Handling statuses:
        READY - allow to submit
        PLAYERS - need to reset gift distribution
        CREATE - raise exception
        SUBMITTED - skipping
    """

    santa = ss_service.get_by_code(santa_code)

    if santa.status == StatusType.CREATED:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Need to add players")

    if santa.status == StatusType.PLAYERS:
        player_service.reset_distribution(santa_code)
        ss_service.update_status(santa_code, StatusType.READY)

    if santa.status == StatusType.READY:
        players = player_service.distribution(santa_code)
        ss_service.update_status(santa_code, StatusType.SUBMITTED)

        message = forming_players_message(santa_code, players)
        send_message_to_queue_task(message)

    return ss_service.get_by_code(santa_code)
