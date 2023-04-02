import logging
from coffee_freaks_api_client.models import CoffeeResultWithRoaster, RoasterResult, RoasterRequestEntity, \
    CoffeeRequestEntity, CoffeeResult
from coffee_freaks_api_client.types import Unset
from .data_client import DataClient


class DataStore:
    __coffees_with_roasters: list[CoffeeResultWithRoaster]
    __roasters: list[RoasterResult]
    __client: DataClient

    logger = logging.getLogger("dataproxy")

    def __init__(self, data_client: DataClient):
        self.__client = data_client
        self.__coffees_with_roasters = data_client.get_all_coffee_with_rosters()
        self.__roasters = data_client.get_all_roasters()

    def save_roaster(self, roaster: RoasterRequestEntity) -> RoasterResult:

        for r in self.__roasters:
            if r.name == roaster.name:
                self.logger.info("Updating roaster %s", r)
                return self.__client.update_roaster(r.id, roaster)

        self.logger.info("Adding roaster %s", roaster)
        added = self.__client.add_roaster(roaster)
        self.__roasters.append(added)
        return added

    def save_coffee(self, roaster: RoasterResult, coffee: CoffeeRequestEntity) -> CoffeeResult:

        for c in self.__coffees_with_roasters:
            if c.name == coffee.name and c.roaster.id == roaster.id:
                self.logger.info("Updating coffee %s", c)
                if c.roasting_dates is type(c.roasting_dates) == list:
                    existing_roasting_dates = []
                    coffee_roasting_dates = []

                    if not isinstance(c.roasting_dates, Unset):
                        existing_roasting_dates = c.roasting_dates

                    if not isinstance(coffee.roasting_dates, Unset):
                        coffee_roasting_dates = coffee.roasting_dates

                    coffee.roasting_dates = set(existing_roasting_dates + coffee_roasting_dates)

                if c.grammage is type(c.grammage) == list:
                    existing_grammage = []
                    coffee_grammage = []

                    if not isinstance(c.grammage, Unset):
                        existing_grammage = c.grammage

                    if not isinstance(coffee.grammage, Unset):
                        coffee_grammage = coffee.grammage

                    coffee.grammage = set(existing_grammage + coffee_grammage)
                return self.__client.update_coffee(roaster.id, c.id, coffee)

        self.logger.info("Adding coffee %s", coffee)
        added = self.__client.add_coffee(roaster.id, coffee)
        result = CoffeeResultWithRoaster(
            added.id,
            roaster,
            added.name,
            added.grammage,
            added.kind,
            added.speciality,
            added.created,
            added.updated,
            added.origin,
            added.beans,
            added.processing,
            added.roasting_level,
            added.dedicated,
            added.description,
            added.roasting_dates
        )
        self.__coffees_with_roasters.append(result)
        return added
