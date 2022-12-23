import logging
from data_client import DataClient
from data_store import DataStore


class DataService:
    __client: DataClient
    __store: DataStore

    logger = logging.getLogger("dataproxy")

    def __init__(self, data_client: DataClient, data_store: DataStore):
        self.__client = data_client
        self.__store = data_store

    def process_data(self):
        return "not yet"
