from typing import List

from fastapi import Depends

from database import schemas
from database.models import SecretSantaCreate
from database.schemas import StatusType
from database.session import Session, get_session
from services.helpers.helper import generate_random_number


class SecretSantaService:
    """ SecretSanta Service """
    MIN_SANTA_CODE_NUMBER = 100000
    MAX_SANTA_CODE_NUMBER = 999999

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[schemas.SecretSanta]:
        """ Getting a list of SecretSanta games """
        santas = (
            self.session
            .query(schemas.SecretSanta)
            .all()
        )
        return santas

    def get_by_code(self, santa_code: int) -> schemas.SecretSanta:
        """ Getting the SecretSanta model by code game """
        santa = (
            self.session
            .query(schemas.SecretSanta)
            .filter_by(code=santa_code)
        ).one()
        return santa

    def create(self, santa_data: SecretSantaCreate) -> schemas.SecretSanta:
        """ Creating the SecretSanta game """
        santa_dict = santa_data.dict()
        santa_code = generate_random_number(
            self.MIN_SANTA_CODE_NUMBER, self.MAX_SANTA_CODE_NUMBER)
        santa_dict['code'] = santa_code
        # TODO add try construct to handle non-unique code value

        santa = schemas.SecretSanta(**santa_dict)
        santa.status = StatusType.CREATED

        self.session.add(santa)
        self.session.commit()

        return santa

    def update_status(self, santa_code: int, status: StatusType):
        """ Updating santa status """
        santa = self.get_by_code(santa_code)

        if santa.status == status:
            return

        santa.status = status
        self.session.add(santa)
        self.session.commit()
