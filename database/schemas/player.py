from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from database.base_class import Base


class Player(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    username = Column(String)
    social_url = Column(String, nullable=False)

    cards = relationship("Card")
    santa_id = Column(Integer, ForeignKey("secretsanta.id"))
