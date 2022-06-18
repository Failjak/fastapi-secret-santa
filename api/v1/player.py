from typing import List, Any

from fastapi import APIRouter, Depends

from services.v1.player import PlayerService
from database.models import Player, PlayerCreate

router = APIRouter(prefix='/player')


@router.post('/', response_model=Player)
def create_player(player_data: PlayerCreate, service: PlayerService = Depends()):
    return service.create(player_data)


@router.get('/list', response_model=List[Player])
def get_players(santa_id: int = None, service: PlayerService = Depends()):
    return service.get_list(santa_id)
