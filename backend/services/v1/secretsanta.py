from typing import List

from fastapi import Depends
from sqlalchemy.exc import IntegrityError

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

        while True:
            santa_code = self.__generate_santa_code()
            santa, uniq = self.__create_new_santa(santa_dict=santa_dict, santa_code=santa_code)
            if uniq:
                break

        return santa

    def __create_new_santa(self, santa_dict: dict, santa_code: int) -> (schemas.SecretSanta, bool):
        """
        Creating new santa instance in DataBase

        return: (santa instance, True/False)
            True - santa code is unique
            False - need to recalculate the santa code
        """
        santa_dict['code'] = santa_code
        santa = schemas.SecretSanta(**santa_dict)

        santa.status = StatusType.CREATED
        self.session.add(santa)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return santa, False

        return santa, True

    def __generate_santa_code(self) -> int:
        """ Generating SecretSanta game code """
        return generate_random_number(
            self.MIN_SANTA_CODE_NUMBER, self.MAX_SANTA_CODE_NUMBER)

    def update_status(self, santa_code: int, status: StatusType):
        """ Updating santa status """
        santa = self.get_by_code(santa_code)

        if santa.status == status:
            return

        santa.status = status
        self.session.add(santa)
        self.session.commit()
