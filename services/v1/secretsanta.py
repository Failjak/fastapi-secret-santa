from typing import List
from fastapi import Depends

from database.session import Session, get_session
from database.models import SecretSanta, SecretSantaCreate
from database import schemas


class SecretSantaService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[SecretSanta]:
        games = (
            self.session
            .query(schemas.SecretSanta)
            .all()
        )

        return games

    def create(self, santa_data: SecretSantaCreate) -> schemas.SecretSanta:
        santa = schemas.SecretSanta(**santa_data.dict())
        self.session.add(santa)
        self.session.commit()
        return santa
