from datetime import datetime
from typing import List

from pydantic import BaseModel

from .base_model import ORMBaseModel
from .player import Player


class SecretSantaBase(BaseModel):
    """ SecreteSanta base model """
    name: str


class SecretSanta(SecretSantaBase, ORMBaseModel):
    """ SecretSanta model with full information """
    id: int
    is_active: bool
    code: int
    created_at: datetime
    updated_at: datetime = None
    players: List[Player] = []


class SecretSantaCreate(SecretSantaBase):
    """ SecretSanta mode with information to create """
    pass
