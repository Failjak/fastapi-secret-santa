from database.models.base_model import ORMBaseModel
from database.schemas import CardType


class Card(ORMBaseModel):
    id: int
    type: CardType
    description: str
    player_id: int
