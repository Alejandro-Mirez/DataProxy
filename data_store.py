import logging
from coffee_freaks_api_client.models import CoffeeResultWithRoaster, RoasterResult, RoasterRequestEntity
from data_client import DataClient


class DataStore:
    __coffees_with_roasters: list[CoffeeResultWithRoaster]
    __roasters: list[RoasterResult]
    __client: DataClient

    logger = logging.getLogger("dataproxy")

    def __init__(self, data_client: DataClient):
        self.__client = data_client
        self.__coffees_with_roasters = data_client.get_all_coffee_with_rosters()
        self.__roasters = data_client.get_all_roasters()

    def save_roaster(self, roaster: RoasterRequestEntity) -> str:

        for r in self.__roasters:
            if r.name == roaster.name:
                self.logger.info("Updating roaster %s", r)
                self.__client.update_roaster(r.id, roaster)
                return r.id

        self.logger.info("Adding roaster %s", roaster)
        added = self.__client.add_roaster(roaster)
        self.__roasters.append(added)
        return added.id
