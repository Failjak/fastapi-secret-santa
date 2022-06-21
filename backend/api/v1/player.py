from typing import List

from fastapi import APIRouter, Depends

from database.models import Player, PlayerCreate
from services.v1.player import PlayerService

router = APIRouter(prefix='/player')


@router.post('/', response_model=Player)
def create_player(player_data: PlayerCreate, service: PlayerService = Depends()):
    """ Creating players """
    return service.create(player_data)


@router.get('/', response_model=List[Player])
def get_players(santa_id: int = None, service: PlayerService = Depends()):
    """ Getting players """
    return service.get_list(santa_id)
