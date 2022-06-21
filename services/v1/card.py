from typing import List

from fastapi import Depends


from database.session import Session, get_session
from database import schemas
from database.models import Card, CardCreate


class CardService:
    """ Card Service """

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, card_data: CardCreate) -> schemas.Card:
        """ Creating the Card """
        card = schemas.Card(**card_data.dict())
        self.session.add(card)
        self.session.commit()
        return card

    def get_list(self, player_id: int) -> List[Card]:
        """ Getting card for this player_id """
        cards = self.session.query(schemas.Card).filter_by(player_id=player_id).all()
        return cards
