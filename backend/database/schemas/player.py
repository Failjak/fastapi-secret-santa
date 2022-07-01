from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from database.schemas.base_class import Base


class Player(Base):
    """ Player DB schema """

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    username = Column(String)
    social_url = Column(String, nullable=False)

    cards = relationship("Card")
    santa_code = Column(Integer, ForeignKey("secretsanta.code"))

    gives_to_id = Column(Integer, ForeignKey("player.id"), nullable=True)
    gives_to = relationship("Player", remote_side="Player.id", backref=backref("gives_from"))
