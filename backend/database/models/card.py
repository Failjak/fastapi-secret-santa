from pydantic import BaseModel

from .base_model import ORMBaseModel
from ..schemas import CardType


class BaseCard(BaseModel):
    """ Base card model """
    type: CardType
    description: str
    player_id: int


class Card(BaseCard, ORMBaseModel):
    """ Card model with full information """
    id: int


class CardCreate(BaseCard):
    """ Card model with information to create """
    pass
