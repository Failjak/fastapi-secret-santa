from typing import List

from pydantic import AnyUrl, BaseModel

from database.models.base_model import ORMBaseModel
from database.models.card import Card


class BasePlayer(BaseModel):
    name: str
    username: str = None
    social_url: AnyUrl
    santa_id: int


class Player(BasePlayer, ORMBaseModel):
    id: int
    cards: List[Card] = []


class PlayerCreate(BasePlayer):
    pass
