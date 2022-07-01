from typing import Union, List

import pymongo.errors
from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from services.db import DBService

config = dotenv_values()


class Config:
    def __init__(self):
        self.config = dotenv_values()


class MongoService(DBService, Config):

    USER_COLLECTION_NAME = 'user'

    def __init__(self):
        super().__init__()
        uri = "mongodb://%s:%s@%s" % (
            self.config.get('MONGO_INITDB_ROOT_USERNAME'),
            self.config.get('MONGO_INITDB_ROOT_PASSWORD'),
            self.config.get("MONGO_HOST")
        )

        self.client = MongoClient(uri)
        self.db = self.client.get_database(self.config.get('MONGO_DB_NAME'))
        self.collect = self.db.get_collection(self.USER_COLLECTION_NAME)

    def __del__(self):
        """ Closed the MongoDB connection """
        self.client.close()

    def insert(self, data: dict) -> int:
        """
        Insert a document into a collection and return doc's id

        :param data: data to add to database
        :returns:
            if inserting was successful -> inserted_id
            if this id existed -> -1
        """
        try:
            return self.collect.insert_one(data).inserted_id
        except DuplicateKeyError:
            return -1

    def extends(self, data: List[dict]) -> List[int]:
        """ Inserting a list of documents into a collection and returning inserted """
        return self.collect.insert_many(data).inserted_ids

    def select(self, elements: dict, multiple: bool = False) -> Union[List[dict], dict]:
        """
        Retrieve single or multiply documents from a collection

        :param elements: dictionary to find for an element\elements.
        :param multiple: Toggle for getting list of elements or single element

        :returns: Optional[List[dict], dict]
        """

        if multiple:
            result = self.collect.find(elements)
            return [r for r in result]
        return self.collect.find_one(elements)

    def update(self, filter: dict, value: dict, multiple: bool = False) -> int:
        """
        Update data which fie passed filter

        :param filter: Filter for data
        :param value: New value for suitable data
        :param multiple: Toggle for updating one or many documents

        :returns: If multiple=True -> count of modified documents, otherwise id of modified id
        """
        if multiple:
            return self.collect.update_many(
                filter=filter,
                update={"$set": value}
            ).modified_count
        return self.collect.update_one(
            filter=filter,
            update={"$set": value}
        ).upserted_id

    def remove(self, filter: dict, multiple: bool = False) -> int:
        """
        Removing data which fit passed filter

        :param filter: Filter for data
        :param multiple: Toggle for deleting all or one element

        :returns: Count of deleted data
        """
        if multiple:
            return self.collect.delete_many(filter).deleted_count
        return self.collect.delete_one(filter).deleted_count

    def clear(self):
        """ Deleting all documents from the collection """
        return self.collect.delete_many({})
