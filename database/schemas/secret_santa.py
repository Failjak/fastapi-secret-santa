from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.base_class import Base


class SecretSanta(Base):
    """ SecretSanta DB schema """

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    is_active = Column(Boolean, default=True)
    name = Column(String(255))
    code = Column(Integer, unique=True, primary_key=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())

    players = relationship("Player")
