from typing import List

from pydantic import BaseModel
from datetime import datetime

from database.models.base_model import BaseModel as DBBaseModel
from database.models.player import Player


class SecretSantaBase(BaseModel):
    name: str


class SecretSanta(SecretSantaBase, DBBaseModel):
    id: str
    is_active: bool
    code: int
    created_at: datetime
    updated_at: datetime
    players: List[Player]


class SecretSantaCreate(SecretSantaBase):
    pass
