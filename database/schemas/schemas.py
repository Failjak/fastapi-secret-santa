from typing import List

from pydantic import BaseModel, UUID1, AnyUrl
from datetime import datetime

from ..models import CardType


class Card(BaseModel):
    id: int
    type: CardType
    description: str
    player_id: int


class Player(BaseModel):
    id: int
    name: str
    username: str
    social_url: AnyUrl
    cards: List[Card]
    santa_id: int


class SecretSanta(BaseModel):
    id: int
    uuid: UUID1
    created_at: datetime
    updated_at: datetime
    players: List[Player]

