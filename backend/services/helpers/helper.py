import random
from typing import Union, List

from pydantic import BaseModel

from database import schemas
from database.models import Player, Card, SecretSanta


def generate_random_number(min_val, max_val):
    """ Generating random number between passed values """
    return random.randrange(min_val, max_val)


def get_model_from_schema(schema: Union[schemas.Player, schemas.Card, schemas.SecretSanta]):
    if isinstance(schema, schemas.Player):
        return Player(**schema.__dict__)
    if isinstance(schema, schemas.Card):
        return Card(**schema.__dict__)
    if isinstance(schema, schemas.SecretSanta):
        return SecretSanta(**schema.__dict__)


def get_dict_from_model(models: List[BaseModel]):
    dict_models = []
    for model in models:
        dict_models.append(model.dict())
    return dict_models

