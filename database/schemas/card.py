from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
import enum

from database.base_class import Base


class CardType(enum.Enum):
    DESIRE = 'DESIRE'
    ANTI_DESIRE = 'ANTI_DESIRE'


class Card(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(Enum(CardType))
    description = Column(Text)
    player_id = Column(Integer, ForeignKey("player.id"))
