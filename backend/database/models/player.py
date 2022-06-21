from typing import List

from pydantic import AnyUrl, BaseModel

from .base_model import ORMBaseModel
from .card import Card


class BasePlayer(BaseModel):
    """ Player base model """
    name: str
    username: str = None
    social_url: AnyUrl
    santa_id: int


class Player(BasePlayer, ORMBaseModel):
    """ Player model with full information"""
    id: int
    cards: List[Card] = []


class PlayerCreate(BasePlayer):
    """ Player model with information to create """
    pass
