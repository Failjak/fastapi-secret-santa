import enum

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.schemas.base_class import Base


class CurrencyType(str, enum.Enum):
    """ Currency types """

    BYN = 'BYN'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'


class StatusType(str, enum.Enum):
    """ Status types """
    CREATED = "CREATED"
    READY = "READY"
    PLAYERS = "PLAYERS"
    SUBMITTED = "SUBMITTED"
    FAILED = "FAILED"


class SecretSanta(Base):
    """ SecretSanta DB schema """

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True
    )
    is_active = Column(Boolean, default=True)
    status = Column(Enum(StatusType))

    name = Column(String(255))
    code = Column(Integer, unique=True, primary_key=True)

    expected_amount = Column(Float, default=None)
    currency_iso3 = Column(Enum(CurrencyType))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())

    players = relationship("Player")
