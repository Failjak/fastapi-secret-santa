from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.base_class import Base


class SecretSanta(Base):
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    # id = Column(
    #     UUID(as_uuid=True),
    #     default=uuid.uuid4,
    #     primary_key=True,
    #     index=True,
    # )
    is_active = Column(Boolean, default=True)
    name = Column(String(255))
    code = Column(Integer, unique=True, primary_key=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())

    players = relationship("Player")


