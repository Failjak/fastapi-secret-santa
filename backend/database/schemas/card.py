import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum, Text

from ..base_class import Base


class CardType(enum.Enum):
    """ Enum with card types """

    DESIRE = 'DESIRE'
    ANTI_DESIRE = 'ANTI_DESIRE'


class Card(Base):
    """ Card DB schema """

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(Enum(CardType))
    description = Column(Text)
    player_id = Column(Integer, ForeignKey("player.id"))
