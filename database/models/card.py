from database.models.base_model import BaseModel
from database.schemas import CardType


class Card(BaseModel):
    id: int
    type: CardType
    description: str
    player_id: int
