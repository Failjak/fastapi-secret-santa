from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..base_class import Base


class SecretSanta(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    players = relationship("Player")
