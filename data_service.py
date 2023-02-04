import logging
from data_client import DataClient
from data_store import DataStore
from coffee_freaks_api_client.models import RoasterRequestEntity
from model import Item
import geonamescache


class DataService:
    __client: DataClient
    __store: DataStore

    logger = logging.getLogger("dataproxy")
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities().values()
    countries = gc.get_countries().values()

    def __init__(self, data_client: DataClient, data_store: DataStore):
        self.__client = data_client
        self.__store = data_store

    def __find_roaster_city(self, country_code: str, item: Item) -> str:
        full_name = item.details["Pełna nazwa producenta:"]

        for city in self.cities:
            city_country_code: str = city['countrycode']

            if city_country_code == country_code:
                city_name: str = city['name']
                alternate_names: list[str] = city['alternatenames']
                if city_name in full_name:
                    self.logger.info(city)
                    return city_name
                if any(alt_name in full_name for alt_name in alternate_names) and alternate_names != ['']:
                    self.logger.info(city)
                    return city_name

        return ""

    def __find_roaster_country(self, item: Item) -> dict:
        full_name = item.details["Pełna nazwa producenta:"].lower()
        tags = item.tags

        for country in self.countries:
            country_name = country['name'].lower()
            if country_name in full_name:
                return country

            for tag in tags:
                tag_name = tag.lower()

                if "polska" in tag_name:
                    return {'name': "Poland", 'iso': 'PL'}

        return {}

    def __create_roaster(self, item: Item) -> RoasterRequestEntity:
        country = self.__find_roaster_country(item)
        self.logger.debug("Found country: %s", country)
        city = self.__find_roaster_city(country['iso'], item)

        return RoasterRequestEntity(
            item.details["Producent:"],
            item.details["Pełna nazwa producenta:"],
            country['name'],
            city
        )

    def process_data(self, item: Item):
        roaster = self.__create_roaster(item)
        roasterId = self.__store.save_roaster(roaster)


        result = {'roasterId': roasterId}
        print(result)
        return result
