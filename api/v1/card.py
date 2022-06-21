from typing import List

from fastapi import APIRouter, Depends

from database.models import Card, CardCreate
from services.v1.card import CardService

router = APIRouter(prefix='/card')


@router.post('/', response_model=Card)
def create_card(card_data: CardCreate, service: CardService = Depends()):
    """ Creating card """
    return service.create(card_data)


@router.get('/', response_model=List[Card])
def get_cards(player_id: int, service: CardService = Depends()):
    """ Getting cards """
    return service.get_list(player_id)
