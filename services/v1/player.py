from typing import List

from fastapi import Depends

from database import schemas
from database.models import Player, PlayerCreate
from database.session import Session, get_session


class PlayerService:
    """ Player Service """
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, player_data: PlayerCreate) -> schemas.Player:
        """ Creating the PLayer """
        player = schemas.Player(**player_data.dict())
        self.session.add(player)
        self.session.commit()
        return player

    def get_list(self, santa_id: int = None) -> List[Player]:
        """ Getting all players by santa_id"""
        query = self.session.query(schemas.Player)
        players = query.filter_by(santa_id=santa_id).all() if santa_id is not None else query.all()

        return players
