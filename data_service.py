from pprint import pprint
from data_client import DataClient


class DataService:
    __client: DataClient

    def __init__(self, data_client: DataClient):
        self.__client = data_client

    def process_data(self):
        return "not yet"
