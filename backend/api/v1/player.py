from typing import List

from fastapi import APIRouter, Depends

from database.models import Player, PlayerCreate
from database.schemas import StatusType
from services.v1.common.routes import ValidationErrorLoggingRoute
from services.v1.player import PlayerService
from services.v1.secretsanta import SecretSantaService

router = APIRouter(prefix='/player', route_class=ValidationErrorLoggingRoute)


@router.post('/players', response_model=List[Player])
def create_player(
        santa_code: int,
        players_data: List[PlayerCreate],
        ss_service: SecretSantaService = Depends(),
        service: PlayerService = Depends()):
    """ Creating players """
    # TODO move status updating to background task
    santa = ss_service.get_by_code(santa_code)
    res_status = StatusType.PLAYERS if santa.status != StatusType.CREATED else StatusType.READY
    ss_service.update_status(santa_code, res_status)

    return service.create(santa_code, players_data)


@router.get('/', response_model=List[Player])
def get_players(santa_code: int, service: PlayerService = Depends()):
    """ Getting players by santa_code """
    return service.get_list(santa_code)
