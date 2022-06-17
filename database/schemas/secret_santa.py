from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from database.base_class import Base


class SecretSanta(Base):
    id = Column(
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
        unique=True,
        index=True,
    )
    is_active = Column(Boolean, default=True)
    name = Column(String(255))
    code = Column(Integer, unique=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    players = relationship("Player")


