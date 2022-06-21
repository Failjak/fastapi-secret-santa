from pydantic import BaseModel

from database.models.base_model import ORMBaseModel
from database.schemas import CardType


class BaseCard(BaseModel):
    type: CardType
    description: str
    player_id: int


class Card(BaseCard, ORMBaseModel):
    id: int


class CardCreate(BaseCard):
    pass
