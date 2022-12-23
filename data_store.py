import logging
from coffee_freaks_api_client.models import CoffeeResultWithRoaster
from data_client import DataClient


class DataStore:
    __data: list[CoffeeResultWithRoaster]
    __client: DataClient

    logger = logging.getLogger("dataproxy")

    def __init__(self, data_client: DataClient):
        self.__client = data_client
        self.__data = data_client.get_all_coffee_with_rosters()
