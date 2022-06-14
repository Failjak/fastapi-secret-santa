from typing import List, Union, Any

import pydantic
from pydantic import UUID1, AnyUrl
from datetime import datetime

from ..models import CardType


class BaseModel(pydantic.BaseModel):
    class Config:
        orm_mode = True


class CardSerializer(BaseModel):
    id: int
    type: CardType
    description: str
    player_id: int


class PlayerSerializer(BaseModel):
    id: int
    name: str
    username: str
    social_url: AnyUrl
    cards: List[CardSerializer]
    santa_id: int


class SecretSantaSerializer(BaseModel):
    id: int
    uuid: UUID1
    created_at: datetime
    updated_at: datetime
    players: List[PlayerSerializer]
