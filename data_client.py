import logging
from http import HTTPStatus
from typing import Union

from coffee_freaks_api_client import Client
from coffee_freaks_api_client.api.all_ import post_api_v1_account_login, post_api_v1_account_token_refresh, \
    get_api_v1_account_logout, get_api_v1_coffee, post_api_v1_roaster, put_api_v1_roaster_roasterid, \
    delete_api_v1_roaster_roasterid, post_api_v1_roaster_roasterid_coffee, put_api_v1_roaster_roasterid_coffee_coffeeid, \
    delete_api_v1_roaster_roasterid_coffee_coffeeid, get_api_v1_roaster_roasterid, \
    get_api_v1_roaster_roasterid_coffee_coffeeid
from math import ceil

from coffee_freaks_api_client.models import LoginRequest, BadRequest, InvalidInput, ServerError, TokenResult, \
    Unauthorized, CoffeeResultWithRoaster, RoasterRequestEntity, CoffeeRequestEntity, RoasterResult, CoffeeResult
from coffee_freaks_api_client.types import Response
from configuration import Settings
from typing import Callable, Any


class DataClient:
    __DEFAULT_LIMIT = 50
    __api: Client
    __settings: Settings
    __auth_token: str
    __refresh_token: str

    logger = logging.getLogger("dataproxy")

    def __init__(self, api_client: Client, settings: Settings):
        self.__api = api_client
        self.__settings = settings
        self.__login()

    def __login(self):
        self.logger.info("Logging in")
        request = LoginRequest(login=self.__settings.api_user, password=self.__settings.api_password)
        response: Union[BadRequest, InvalidInput, ServerError, TokenResult, None] = post_api_v1_account_login.sync(
            json_body=request, client=self.__api)
        if isinstance(response, TokenResult):
            self.logger.debug("User logged in")
            self.__auth_token = response.auth_token
            self.__refresh_token = response.refresh_token
        elif isinstance(response, BadRequest | InvalidInput | ServerError):
            raise response.error

    def __refresh(self):
        self.logger.info("Refreshing")
        response: Union[
            BadRequest, ServerError, TokenResult, Unauthorized, None] = post_api_v1_account_token_refresh.sync(
            x_coffee_refresh_auth=self.__refresh_token, client=self.__api)
        if isinstance(response, TokenResult):
            self.logger.debug("User refreshed")
            self.__auth_token = response.auth_token
            self.__refresh_token = response.refresh_token
        elif isinstance(response, BadRequest | Unauthorized | ServerError):
            raise response.error

    def __safe_call(self, f):
        response = f()
        if isinstance(response, Unauthorized) or (
                isinstance(response, Response) and response.status_code == HTTPStatus.UNAUTHORIZED):
            self.__refresh()
            response = f()
        if isinstance(response, BadRequest) or isinstance(response, ServerError):
            raise response
        return response

    def logout(self):
        self.logger.info("Logging out")
        get_api_v1_account_logout.sync(x_coffee_auth=self.__auth_token, x_coffee_refresh_auth=self.__refresh_token,
                                       client=self.__api)

    def get_all_coffee_with_rosters(self) -> list[CoffeeResultWithRoaster]:
        self.logger.info("Fetching all coffee with roasters")
        results = []

        def __get_page(page: int, limit: int = self.__DEFAULT_LIMIT):
            self.logger.debug(f"Fetching page {page}")
            result = self.__safe_call(
                lambda *args: get_api_v1_coffee.sync(
                    limit=limit,
                    offset=limit * page,
                    client=self.__api
                )
            )
            self.logger.debug(result)
            return result

        first_result = __get_page(0)
        results.append(first_result.results)
        pages = ceil(first_result.count / self.__DEFAULT_LIMIT)
        for page in range(1, pages):
            page_result = __get_page(page)
            results.append(page_result.results)

        return results

    def __call_and_fetch(self, f: Callable[[], Response[Any]], g: Callable[[str], Any]):
        result = f()
        self.logger.debug(f"Result returned: {result.status_code}")
        if result.status_code == HTTPStatus.NO_CONTENT or result.status_code == HTTPStatus.CREATED:
            location = result.headers.get("location")
            if location is not None:
                self.logger.debug(f"Moving to: {location}")
                return g(location.split("/")[-1])
            else:
                raise result
        else:
            raise result

    def get_roaster(self, id: str) -> RoasterResult:
        self.logger.info("Get roaster")
        result = self.__safe_call(lambda *args: get_api_v1_roaster_roasterid.sync(roaster_id=id, client=self.__api))
        self.logger.debug(result)
        return result

    def add_roaster(self, roster: RoasterRequestEntity) -> RoasterResult:
        self.logger.info("Add roaster")

        result = self.__call_and_fetch(
            lambda *args: self.__safe_call(
                lambda *args: post_api_v1_roaster.sync_detailed(json_body=roster, x_coffee_auth=self.__auth_token,
                                                                client=self.__api)
            ),
            lambda id: self.get_roaster(id)
        )
        self.logger.debug(result)
        return result

    def update_roaster(self, roaster_id: str, roster: RoasterRequestEntity) -> RoasterResult:
        self.logger.info(f"Update roaster {roaster_id}")

        result = self.__call_and_fetch(
            lambda *args: self.__safe_call(
                lambda *args: put_api_v1_roaster_roasterid.sync_detailed(
                    json_body=roster,
                    roaster_id=roaster_id,
                    x_coffee_auth=self.__auth_token,
                    client=self.__api
                )
            ),
            lambda id: self.get_roaster(id)
        )
        self.logger.debug(result)
        return result

    def delete_roaster(self, roaster_id: str):
        self.logger.info(f"Delete roaster {roaster_id}")
        result = self.__safe_call(
            lambda *args: delete_api_v1_roaster_roasterid.sync_detailed(
                roaster_id=roaster_id,
                x_coffee_auth=self.__auth_token,
                client=self.__api
            )
        )
        self.logger.debug(result)
        return result

    def get_coffee(self, roaster_id: str, coffee_id: str) -> CoffeeResult:
        self.logger.info(f"Get coffee {coffee_id} on roaster {roaster_id}")
        result = self.__safe_call(
            lambda *args: get_api_v1_roaster_roasterid_coffee_coffeeid.sync(roaster_id=roaster_id, coffee_id=coffee_id,
                                                                            client=self.__api))
        self.logger.debug(result)
        return result

    def add_coffee(self, roaster_id: str, coffee: CoffeeRequestEntity) -> CoffeeResult:
        self.logger.info("Adding coffee")
        result = self.__call_and_fetch(
            lambda *args: self.__safe_call(
                lambda *args: post_api_v1_roaster_roasterid_coffee.sync_detailed(
                    json_body=coffee,
                    roaster_id=roaster_id,
                    x_coffee_auth=self.__auth_token,
                    client=self.__api
                )
            ),
            lambda id: self.get_coffee(roaster_id, id)
        )
        self.logger.debug(result)
        return result

    def update_coffee(self, roaster_id: str, coffee_id: str, coffee: CoffeeRequestEntity) -> CoffeeResult:
        self.logger.info(f"Updating coffee {coffee_id} in roaster {roaster_id}")
        result = self.__call_and_fetch(
            lambda *args: self.__safe_call(
                lambda *args: put_api_v1_roaster_roasterid_coffee_coffeeid.sync_detailed(
                    json_body=coffee,
                    roaster_id=roaster_id,
                    coffee_id=coffee_id,
                    x_coffee_auth=self.__auth_token,
                    client=self.__api
                )
            ),
            lambda id: self.get_coffee(roaster_id, id)
        )
        self.logger.debug(result)
        return result

    def delete_coffee(self, roaster_id: str, coffee_id: str):
        self.logger.info(f"Deleting coffee {coffee_id} in roaster {roaster_id}")
        result = self.__safe_call(
            lambda *args: delete_api_v1_roaster_roasterid_coffee_coffeeid.sync(
                roaster_id=roaster_id,
                coffee_id=coffee_id,
                x_coffee_auth=self.__auth_token,
                client=self.__api
            )
        )
        self.logger.debug(result)

        return result
