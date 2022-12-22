import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_v1_account_login import ApiV1AccountLogin
from openapi_client.apis.paths.api_v1_account_logout import ApiV1AccountLogout
from openapi_client.apis.paths.api_v1_account_register import ApiV1AccountRegister
from openapi_client.apis.paths.api_v1_account_register_resend import ApiV1AccountRegisterResend
from openapi_client.apis.paths.api_v1_account_register_verify import ApiV1AccountRegisterVerify
from openapi_client.apis.paths.api_v1_account_password_reset import ApiV1AccountPasswordReset
from openapi_client.apis.paths.api_v1_account_password_reset_verify import ApiV1AccountPasswordResetVerify
from openapi_client.apis.paths.api_v1_account_token_refresh import ApiV1AccountTokenRefresh
from openapi_client.apis.paths.api_v1_account_token_verify import ApiV1AccountTokenVerify
from openapi_client.apis.paths.api_v1_roaster import ApiV1Roaster
from openapi_client.apis.paths.api_v1_roaster_roaster_id import ApiV1RoasterRoasterId
from openapi_client.apis.paths.api_v1_roaster_roaster_id_coffee import ApiV1RoasterRoasterIdCoffee
from openapi_client.apis.paths.api_v1_roaster_roaster_id_coffee_coffee_id import ApiV1RoasterRoasterIdCoffeeCoffeeId
from openapi_client.apis.paths.api_v1_coffee import ApiV1Coffee

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_ACCOUNT_LOGIN: ApiV1AccountLogin,
        PathValues.API_V1_ACCOUNT_LOGOUT: ApiV1AccountLogout,
        PathValues.API_V1_ACCOUNT_REGISTER: ApiV1AccountRegister,
        PathValues.API_V1_ACCOUNT_REGISTER_RESEND: ApiV1AccountRegisterResend,
        PathValues.API_V1_ACCOUNT_REGISTER_VERIFY: ApiV1AccountRegisterVerify,
        PathValues.API_V1_ACCOUNT_PASSWORD_RESET: ApiV1AccountPasswordReset,
        PathValues.API_V1_ACCOUNT_PASSWORD_RESET_VERIFY: ApiV1AccountPasswordResetVerify,
        PathValues.API_V1_ACCOUNT_TOKEN_REFRESH: ApiV1AccountTokenRefresh,
        PathValues.API_V1_ACCOUNT_TOKEN_VERIFY: ApiV1AccountTokenVerify,
        PathValues.API_V1_ROASTER: ApiV1Roaster,
        PathValues.API_V1_ROASTER_ROASTER_ID: ApiV1RoasterRoasterId,
        PathValues.API_V1_ROASTER_ROASTER_ID_COFFEE: ApiV1RoasterRoasterIdCoffee,
        PathValues.API_V1_ROASTER_ROASTER_ID_COFFEE_COFFEE_ID: ApiV1RoasterRoasterIdCoffeeCoffeeId,
        PathValues.API_V1_COFFEE: ApiV1Coffee,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_ACCOUNT_LOGIN: ApiV1AccountLogin,
        PathValues.API_V1_ACCOUNT_LOGOUT: ApiV1AccountLogout,
        PathValues.API_V1_ACCOUNT_REGISTER: ApiV1AccountRegister,
        PathValues.API_V1_ACCOUNT_REGISTER_RESEND: ApiV1AccountRegisterResend,
        PathValues.API_V1_ACCOUNT_REGISTER_VERIFY: ApiV1AccountRegisterVerify,
        PathValues.API_V1_ACCOUNT_PASSWORD_RESET: ApiV1AccountPasswordReset,
        PathValues.API_V1_ACCOUNT_PASSWORD_RESET_VERIFY: ApiV1AccountPasswordResetVerify,
        PathValues.API_V1_ACCOUNT_TOKEN_REFRESH: ApiV1AccountTokenRefresh,
        PathValues.API_V1_ACCOUNT_TOKEN_VERIFY: ApiV1AccountTokenVerify,
        PathValues.API_V1_ROASTER: ApiV1Roaster,
        PathValues.API_V1_ROASTER_ROASTER_ID: ApiV1RoasterRoasterId,
        PathValues.API_V1_ROASTER_ROASTER_ID_COFFEE: ApiV1RoasterRoasterIdCoffee,
        PathValues.API_V1_ROASTER_ROASTER_ID_COFFEE_COFFEE_ID: ApiV1RoasterRoasterIdCoffeeCoffeeId,
        PathValues.API_V1_COFFEE: ApiV1Coffee,
    }
)
