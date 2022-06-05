from typing import Union, List

from pydantic import BaseModel, HttpUrl


class User(BaseModel):
    pass


class Player(BaseModel):
    name: str = None
    social_url: HttpUrl
    username: Union[str, None] = None


class Budget(BaseModel):
    budget: float
    currency: str = "USD"


class SecretSanta(BaseModel):
    players: List[Player]
    organizer: User