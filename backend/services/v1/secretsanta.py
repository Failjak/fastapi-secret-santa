import random
from typing import List

from fastapi import Depends

from database import schemas
from database.models import SecretSanta, SecretSantaCreate
from database.session import Session, get_session


class SecretSantaService:
    """ SecretSanta Service """
    MIN_SANTA_CODE_NUMBER = 100000
    MAX_SANTA_CODE_NUMBER = 999999

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[SecretSanta]:
        """ Getting a list of SecretSanta games """
        games = (
            self.session
            .query(schemas.SecretSanta)
            .all()
        )

        return games

    def create(self, santa_data: SecretSantaCreate) -> schemas.SecretSanta:
        """ Creating the SecretSanta game """
        santa_dict = santa_data.dict()
        santa_dict['code'] = self._generate_game_code()

        santa = schemas.SecretSanta(**santa_dict)
        self.session.add(santa)
        self.session.commit()
        return santa

    def _generate_game_code(self):
        return random.randrange(self.MIN_SANTA_CODE_NUMBER, self.MAX_SANTA_CODE_NUMBER)
