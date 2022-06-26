from abc import ABC
from typing import List, Union


class DBService(ABC):
    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def insert(self, data: dict) -> int:
        """ Insert a document into a collection and return doc's id """
        raise NotImplementedError

    def extends(self, data: List[dict]) -> List[int]:
        """ Inserting a list of documents into a collection and returning inserted """
        raise NotImplementedError

    def select(self, elements: dict, multiple: bool = False) -> Union[List[dict], dict]:
        raise NotImplementedError

    def update(self, filter: dict, value: dict, multiple: bool = False):
        """ Update data which fie passed filter """
        raise NotImplementedError

    def remove(self, filter: dict, multiple: bool = False):
        """ Removing data which fit passed filter """
        raise NotImplementedError

    def clear(self):
        """ Clear all data """
        raise NotImplementedError
