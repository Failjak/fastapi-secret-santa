import random
from typing import List

from fastapi import Depends
from sqlalchemy.orm import load_only

from database import schemas
from database.models import PlayerCreate
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

    def get_list(self, santa_code: int, fields: list = None) -> List[schemas.Player]:
        """ Getting all players by santa_id """

        fields = [] if fields is None else fields
        players = (
            self.session
            .query(schemas.Player)
            .options(load_only(*fields))
            .filter_by(santa_code=santa_code)
            .all()
        )
        return players

    def distribution(self, santa_code: int = None) -> List[schemas.Player]:
        """ Distribution of gifts """

        players = self.get_list(santa_code, fields=['id', 'gives_to_id'])
        players_ids = [player.id for player in players]

        for player in players:

            # TODO skip id if this player gives gift to the current player
            # id_to_skip = player.gives_from[0].id
            # current_ids = players_ids[:]
            # if id_to_skip in current_ids:
            #     current_ids.remove(player.gives_from[0].id)

            # id_to_gives = random.choice(players_ids)
            # while id_to_gives == player.id:
            #     id_to_gives = random.choice(players_ids)
            #
            # players_ids.remove(id_to_gives)
            #
            # player.gives_to_id = id_to_gives
            self.session.add(player)

        self.session.commit()
        return players
