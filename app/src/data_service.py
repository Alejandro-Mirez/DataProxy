import logging
from typing import Union

from coffee_freaks_api_client.types import UNSET, Unset
from .data_client import DataClient
from .data_store import DataStore
from coffee_freaks_api_client.models import RoasterRequestEntity, CoffeeRequestEntity, Beans, UnitType, Grammage, \
    Processing, CoffeeKind, BeansKind, BrewingMethod
from .model import Item, Result
from datetime import date
import geonamescache


class DataService:
    __client: DataClient
    __store: DataStore

    logger = logging.getLogger("dataproxy")
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities().values()
    countries = gc.get_countries().values()

    def __init__(self, data_store: DataStore):
        self.__store = data_store

    def __find_roaster_city(self, country_code: str, item: Item) -> Union[Unset, str]:
        full_address = item.details["Pełna nazwa producenta:"]

        for city in self.cities:
            city_country_code: str = city['countrycode']

            if city_country_code == country_code:
                city_name: str = city['name']
                alternate_names: list[str] = city['alternatenames']
                if city_name in full_address:
                    self.logger.info(city)
                    return city_name
                if any(alt_name in full_address for alt_name in alternate_names) and alternate_names != ['']:
                    self.logger.info(city)
                    return city_name

        return UNSET

    def __find_roaster_country(self, item: Item) -> Union[Unset, dict]:
        full_address = item.details["Pełna nazwa producenta:"].lower()
        self.logger.info("Looking for country in [%s]", full_address)
        tags = item.tags

        if 'england' in full_address:
            return {'name': "United Kingdom", 'iso': 'GB'}

        for country in self.countries:
            country_name = country['name'].lower()
            if country_name in full_address:
                return country

            for tag in tags:
                tag_name = tag.lower()

                if "polska" in tag_name:
                    return {'name': "Poland", 'iso': 'PL'}
                elif "england" in tag_name:
                    return {'name': "United Kingdom", 'iso': 'GB'}

        return UNSET

    def __create_roaster(self, item: Item) -> RoasterRequestEntity:
        country = self.__find_roaster_country(item)
        country_name = UNSET
        city = UNSET
        if not isinstance(country, Unset):
            self.logger.debug("Found country: %s", country)
            city = self.__find_roaster_city(country['iso'], item)
            country_name = country['name']

        return RoasterRequestEntity(
            name=item.details["Producent:"],
            full_address=item.details["Pełna nazwa producenta:"],
            country=country_name,
            city=city
        )

    def __get_coffee_name(self, item: Item) -> str:
        producer = item.details["Producent:"]
        title = item.title
        name = title.replace(producer, "")

        if name[1] == "-":
            new_name = name.strip()
            result = "" + new_name[1:]
            return result.strip()

        return name.strip()

    def __is_speciality(self, item: Item) -> bool:
        speciality = ["speciality", "specialty"]

        if any(spec in item.tags for spec in speciality):
            return True
        if any(spec in item.description for spec in speciality):
            return True

        return False

    def __get_roasting_level(self, item: Item) -> Union[Unset, int]:
        if "Stopień palenia ziaren:" in item.details:
            if item.details["Stopień palenia ziaren:"] == "Jasny":
                return 2
            elif item.details["Stopień palenia ziaren:"] == "Średni":
                return 5
            elif item.details["Stopień palenia ziaren:"] == "Ciemny":
                return 8
        else:
            return UNSET

    def __get_roasting_date(self, item: Item) -> Union[Unset, list[date]]:
        roasting_date = item.roasting_date
        if roasting_date is not None:
            date_list = roasting_date.split(".")
            year = int(date_list[-1])
            month = int(date_list[-2])
            day = int(date_list[-3])
            result = [
                date(year, month, day)
            ]
            return result
        return UNSET

    def __get_origin(self, item: Item) -> Union[Unset, list]:
        if "Pochodzenie:" in item.details:
            origin = item.details["Pochodzenie:"]

            if "," in origin:
                origin_list = origin.split(", ")
            else:
                origin_list = []
                origin_list.append(origin)

            return origin_list
        return UNSET

    def __get_beans(self, item: Item) -> list[Beans]:
        possible_values = {
            'Arabica': Beans(BeansKind.ARABICA, 1),
            'Robusta': Beans(BeansKind.ROBUSTA, 1),
            'Liberica': Beans(BeansKind.LIBERICA, 1),
        }
        beans = item.details["Arabica / Robusta:"]
        beans_list = []

        if "/" in beans:
            split_beans = beans.split("/")
            beans_list.append(Beans(BeansKind.ARABICA, int(split_beans[0]) / 100))
            beans_list.append(Beans(BeansKind.ROBUSTA, int(split_beans[1]) / 100))
        else:
            for value in possible_values.items():
                (key, bean) = value
                if key in beans:
                    beans_list.append(bean)

        return beans_list

    def __get_processing(self, item: Item) -> Union[Unset, list[Processing]]:
        if "Obróbka:" in item.details:
            processing = item.details["Obróbka:"]
            processing_list = []

            if " i " in processing:
                processings = processing.split(" i ")
                for processing in processings:
                    for processing_value in list(Processing):
                        if processing_value.value == processing.lower():
                            processing_list.append(processing_value)
            else:
                for processing_value in list(Processing):
                    if processing_value.value == processing.lower():
                        processing_list.append(processing_value)

            return processing_list
        return UNSET

    def __get_dedication(self, item: Item) -> list[BrewingMethod]:
        dedication = item.details["Przeznaczenie:"]
        dedication_list = []

        if " i " in dedication:
            dedication_list.append(BrewingMethod.DRIP)
            dedication_list.append(BrewingMethod.ESPRESSO)
        else:
            if "drip" in dedication.lower():
                dedication_list.append(BrewingMethod.DRIP)
            elif "espresso" in dedication.lower():
                dedication_list.append(BrewingMethod.ESPRESSO)

        return dedication_list

    def __get_grammage(self, item: Item) -> list[Grammage]:
        grammage = item.details["Opakowanie:"].replace(" ", "")
        value = ""
        unit = ""

        for i in grammage:
            if i.isnumeric():
                value += i
            else:
                unit += i

        if unit == "g":
            return [Grammage(int(value), UnitType.GRAM)]
        elif unit == "kg":
            return [Grammage(int(value), UnitType.KG)]
        else:
            return [Grammage(int(value), UnitType.PIECE)]

    def __get_kind(self, item: Item) -> CoffeeKind:
        kind = item.details["Rodzaj kawy:"]

        if "iarnista" in kind:
            return CoffeeKind.BEANS
        elif "ielona" in kind:
            return CoffeeKind.GROUND
        elif "apsułk" in kind:
            return CoffeeKind.CAPSULES
        elif "ozpuszczalna" in kind or "nstant" in kind:
            return CoffeeKind.INSTANT

    def __create_coffee(self, item: Item) -> CoffeeRequestEntity:
        name = self.__get_coffee_name(item)
        grammage = self.__get_grammage(item)
        kind = self.__get_kind(item)
        speciality = self.__is_speciality(item)
        origin = self.__get_origin(item)
        beans = self.__get_beans(item)
        processing = self.__get_processing(item)
        roasting_level = self.__get_roasting_level(item)
        dedicated = self.__get_dedication(item)
        description = item.description
        roasting_dates = self.__get_roasting_date(item)

        return CoffeeRequestEntity(
            name=name, grammage=grammage, kind=kind, speciality=speciality, origin=origin, beans=beans,
            processing=processing,
            roasting_level=roasting_level, dedicated=dedicated, description=description, roasting_dates=roasting_dates
        )

    def process_data(self, item: Item):
        roaster = self.__create_roaster(item)
        roaster_result = self.__store.save_roaster(roaster)

        coffee = self.__create_coffee(item)
        coffee_result = self.__store.save_coffee(roaster_result, coffee)

        result = Result(roaster_id=roaster_result.id, coffee_id=coffee_result.id)
        return result
