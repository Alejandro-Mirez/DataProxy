import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.all_api import AllApi
from openapi_client.apis.tags.account_account_api import AccountAccountApi
from openapi_client.apis.tags.register_account_register_api import RegisterAccountRegisterApi
from openapi_client.apis.tags.password_account_password_api import PasswordAccountPasswordApi
from openapi_client.apis.tags.token_account_token_api import TokenAccountTokenApi
from openapi_client.apis.tags.roaster_roaster_api import RoasterRoasterApi
from openapi_client.apis.tags.roaster_coffee_roaster_roaster_id_coffee_api import RoasterCoffeeRoasterRoasterIdCoffeeApi
from openapi_client.apis.tags.coffee_coffee_api import CoffeeCoffeeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ALL: AllApi,
        TagValues.ACCOUNT___ACCOUNT_: AccountAccountApi,
        TagValues.REGISTER___ACCOUNT_REGISTER_: RegisterAccountRegisterApi,
        TagValues.PASSWORD___ACCOUNT_PASSWORD: PasswordAccountPasswordApi,
        TagValues.TOKEN___ACCOUNT_TOKEN: TokenAccountTokenApi,
        TagValues.ROASTER___ROASTER_: RoasterRoasterApi,
        TagValues.ROASTER_COFFEE___ROASTER_ROASTER_ID_COFFEE: RoasterCoffeeRoasterRoasterIdCoffeeApi,
        TagValues.COFFEE___COFFEE_: CoffeeCoffeeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ALL: AllApi,
        TagValues.ACCOUNT___ACCOUNT_: AccountAccountApi,
        TagValues.REGISTER___ACCOUNT_REGISTER_: RegisterAccountRegisterApi,
        TagValues.PASSWORD___ACCOUNT_PASSWORD: PasswordAccountPasswordApi,
        TagValues.TOKEN___ACCOUNT_TOKEN: TokenAccountTokenApi,
        TagValues.ROASTER___ROASTER_: RoasterRoasterApi,
        TagValues.ROASTER_COFFEE___ROASTER_ROASTER_ID_COFFEE: RoasterCoffeeRoasterRoasterIdCoffeeApi,
        TagValues.COFFEE___COFFEE_: CoffeeCoffeeApi,
    }
)
