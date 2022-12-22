from pprint import pprint
from frozendict import frozendict
import openapi_client
from configuration import Settings
from openapi_client.apis.tags import account_account_api
from openapi_client.apis.tags import roaster_roaster_api
from openapi_client.apis.tags import coffee_coffee_api
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
from openapi_client.model.login_request import LoginRequest


class DataClient:
    __AUTH_TOKEN_NAME = "X-Coffee-Auth"
    __REFRESH_TOKEN_NAME = "X-Coffee-Refresh-Auth"

    __api_client: openapi_client.ApiClient
    __settings: Settings
    __auth_token: str
    __refresh_token: str
    __account_api: account_account_api.AccountAccountApi
    __roaster_api: roaster_roaster_api.RoasterRoasterApi
    __coffee_api: coffee_coffee_api.CoffeeCoffeeApi
    __roaster_coffee_api: roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi

    def __init__(self, api_client: openapi_client.ApiClient, settings: Settings):
        self.__api_client = api_client
        self.__settings = settings
        self.__account_api = account_account_api.AccountAccountApi(api_client)
        self.__roaster_api = roaster_roaster_api.RoasterRoasterApi(api_client)
        self.__coffee_api = coffee_coffee_api.CoffeeCoffeeApi(api_client)
        self.__roaster_coffee_api = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(
            api_client)
        self.__login()

    def __auth_headers(self):
        return frozendict({self.__AUTH_TOKEN_NAME: self.__auth_token})

    def __login(self):
        try:
            request = LoginRequest(login=self.__settings.api_user, password=self.__settings.api_password)
            response = self.__account_api.post_api_v1_account_login(body=request)
            self.__auth_token = response.body.authToken
            self.__refresh_token = response.body.refreshToken
            pprint("User logged in")
        except openapi_client.ApiException as e:
            print("Exception when calling Logging user: %s\n" % e)
            raise e

    def __refresh(self):
        try:
            response = self.__account_api.post_api_v1_account_token_refresh(
                header_params=frozendict({self.__REFRESH_TOKEN_NAME: self.__refresh_token}))
            self.__auth_token = response.body.authToken
            self.__refresh_token = response.body.refreshToken
        except openapi_client.ApiException as e:
            print("Exception when calling Refresh session: %s\n" % e)
            raise e

    def __safe_call(self, f):
        try:
            return f()
        except openapi_client.ApiException as e:
            if e.status == 401:
                pprint("Refreshing user and trying once again")
                self.__refresh()
                return f()
            else:
                raise e

    def logout(self):
        pprint("Logging out")
        try:
            self.__account_api.get_api_v1_account_logout(header_params=frozendict(
                {self.__AUTH_TOKEN_NAME: self.__auth_token, self.__REFRESH_TOKEN_NAME: self.__refresh_token}))
        except openapi_client.ApiException as e:
            print("Exception when calling Logout: %s\n" % e)
            raise e
