import random
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import load_only

from database import schemas
from database.models import PlayerCreate
from database.session import Session, get_session


class PlayerService:
    """ Player Service """
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, santa_code: int, players_data: List[PlayerCreate]) -> List[schemas.Player]:
        """ Creating the Player """
        players = []
        for player_data in players_data:
            player = schemas.Player(**player_data.dict(), santa_code=santa_code)
            players.append(player)
            self.session.add(player)
        self.session.commit()
        return players

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

    def distribution(self, santa_code: int) -> List[schemas.Player]:
        """ Distribution of gifts """

        players = self.get_list(santa_code, fields=['id', 'gives_to_id'])
        if len(players) <= 2:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Count of users need be more than 2")

        players_ids = [player.id for player in players]
        used_ids = []

        for player in players:
            gives_from_id = [pl.id for pl in player.gives_from]
            ids_to_skip = [player.id, player.gives_to_id] + gives_from_id + used_ids
            available_ids = [id for id in players_ids if id not in ids_to_skip]

            random_id = random.choice(available_ids)
            used_ids.append(random_id)

            player.gives_to_id = random_id
            self.session.add(player)

        self.session.commit()
        return players

    def reset_distribution(self, santa_code: int):
        """ Resetting gift distribution """

        players = self.get_list(santa_code)
        for player in players:
            player.gives_to_id = None
            self.session.add(player)

        self.session.commit()
