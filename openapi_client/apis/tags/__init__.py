# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ALL = "All"
    ACCOUNT___ACCOUNT_ = "Account - /account/"
    REGISTER___ACCOUNT_REGISTER_ = "Register - /account/register/"
    PASSWORD___ACCOUNT_PASSWORD = "Password - /account/password"
    TOKEN___ACCOUNT_TOKEN = "Token - /account/token"
    ROASTER___ROASTER_ = "Roaster - /roaster/"
    ROASTER_COFFEE___ROASTER_ROASTER_ID_COFFEE = "Roaster coffee - /roaster/{roasterId}/coffee"
    COFFEE___COFFEE_ = "Coffee - /coffee/"
