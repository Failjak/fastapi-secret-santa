from typing import List

from pydantic import AnyUrl, BaseModel

from database.models.base_model import ORMBaseModel
from database.models.card import Card


class BasePlayer(BaseModel):
    """ Player base model """
    name: str
    username: str = None
    social_url: AnyUrl


class Player(BasePlayer, ORMBaseModel):
    """ Player model with full information"""
    id: int
    cards: List[Card] = []
    gives_to_id: int = None
    santa_code: int = None


class PlayerCreate(BasePlayer):
    """ Player model with information to create """
    pass


class PlayerMessage(BasePlayer):
    """ PlayerMessage model """
    gives_to: BasePlayer
