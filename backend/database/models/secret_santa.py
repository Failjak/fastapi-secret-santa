from datetime import datetime

from pydantic import BaseModel
from pydantic.fields import Optional, List

from database.models.base_model import ORMBaseModel
from database.models.player import Player
from database.schemas.secret_santa import CurrencyType, StatusType


class SecretSantaBase(BaseModel):
    """ SecreteSanta base model """
    name: str
    expected_amount: Optional[float] = None
    currency_iso3: Optional[CurrencyType]

    # @validator('currency_iso3', pre=True)
    # def validate_enum_field(cls, field: str):
    #     if hasattr(CurrencyType, str(field)):
    #         return CurrencyType(field)
    #     return None


class SecretSanta(SecretSantaBase, ORMBaseModel):
    """ SecretSanta model with full information """
    id: int
    is_active: bool
    code: int
    created_at: datetime
    updated_at: datetime = None
    players: List[Player] = []
    currency_iso3: Optional[CurrencyType] = None
    status: Optional[StatusType]


class SecretSantaCreate(SecretSantaBase):
    """ SecretSanta mode with information to create """
    pass
