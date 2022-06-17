from typing import List

from pydantic import AnyUrl

from database.models.base_model import BaseModel
from database.models.card import Card


class Player(BaseModel):
    id: int
    name: str
    username: str
    social_url: AnyUrl
    cards: List[Card]
    santa_id: int
