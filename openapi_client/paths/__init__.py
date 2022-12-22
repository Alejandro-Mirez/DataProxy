# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_ACCOUNT_LOGIN = "/api/v1/account/login"
    API_V1_ACCOUNT_LOGOUT = "/api/v1/account/logout"
    API_V1_ACCOUNT_REGISTER = "/api/v1/account/register"
    API_V1_ACCOUNT_REGISTER_RESEND = "/api/v1/account/register/resend"
    API_V1_ACCOUNT_REGISTER_VERIFY = "/api/v1/account/register/verify"
    API_V1_ACCOUNT_PASSWORD_RESET = "/api/v1/account/password/reset"
    API_V1_ACCOUNT_PASSWORD_RESET_VERIFY = "/api/v1/account/password/reset/verify"
    API_V1_ACCOUNT_TOKEN_REFRESH = "/api/v1/account/token/refresh"
    API_V1_ACCOUNT_TOKEN_VERIFY = "/api/v1/account/token/verify"
    API_V1_ROASTER = "/api/v1/roaster"
    API_V1_ROASTER_ROASTER_ID = "/api/v1/roaster/{roasterId}"
    API_V1_ROASTER_ROASTER_ID_COFFEE = "/api/v1/roaster/{roasterId}/coffee"
    API_V1_ROASTER_ROASTER_ID_COFFEE_COFFEE_ID = "/api/v1/roaster/{roasterId}/coffee/{coffeeId}"
    API_V1_COFFEE = "/api/v1/coffee"
