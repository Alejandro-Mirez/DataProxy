<a name="__pageTop"></a>
# openapi_client.apis.tags.all_api.AllApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_roaster_roasterid**](#delete_api_v1_roaster_roasterid) | **delete** /api/v1/roaster/{roasterId} | 
[**delete_api_v1_roaster_roasterid_coffee_coffeeid**](#delete_api_v1_roaster_roasterid_coffee_coffeeid) | **delete** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**get_api_v1_account_logout**](#get_api_v1_account_logout) | **get** /api/v1/account/logout | Logout user
[**get_api_v1_account_register_verify**](#get_api_v1_account_register_verify) | **get** /api/v1/account/register/verify | Verify registration token and activate user account
[**get_api_v1_coffee**](#get_api_v1_coffee) | **get** /api/v1/coffee | 
[**get_api_v1_roaster**](#get_api_v1_roaster) | **get** /api/v1/roaster | 
[**get_api_v1_roaster_roasterid**](#get_api_v1_roaster_roasterid) | **get** /api/v1/roaster/{roasterId} | 
[**get_api_v1_roaster_roasterid_coffee**](#get_api_v1_roaster_roasterid_coffee) | **get** /api/v1/roaster/{roasterId}/coffee | 
[**get_api_v1_roaster_roasterid_coffee_coffeeid**](#get_api_v1_roaster_roasterid_coffee_coffeeid) | **get** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**patch_api_v1_roaster_roasterid**](#patch_api_v1_roaster_roasterid) | **patch** /api/v1/roaster/{roasterId} | 
[**patch_api_v1_roaster_roasterid_coffee_coffeeid**](#patch_api_v1_roaster_roasterid_coffee_coffeeid) | **patch** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**post_api_v1_account_login**](#post_api_v1_account_login) | **post** /api/v1/account/login | Login user
[**post_api_v1_account_password_reset**](#post_api_v1_account_password_reset) | **post** /api/v1/account/password/reset | Send reset password link to user account
[**post_api_v1_account_password_reset_verify**](#post_api_v1_account_password_reset_verify) | **post** /api/v1/account/password/reset/verify | Verify user reset password token and change a password
[**post_api_v1_account_register**](#post_api_v1_account_register) | **post** /api/v1/account/register | Register new user and sends email to user for verification
[**post_api_v1_account_register_resend**](#post_api_v1_account_register_resend) | **post** /api/v1/account/register/resend | Creates new token and sends it to user
[**post_api_v1_account_token_refresh**](#post_api_v1_account_token_refresh) | **post** /api/v1/account/token/refresh | Refresh auth token
[**post_api_v1_account_token_verify**](#post_api_v1_account_token_verify) | **post** /api/v1/account/token/verify | Verify user session
[**post_api_v1_roaster**](#post_api_v1_roaster) | **post** /api/v1/roaster | 
[**post_api_v1_roaster_roasterid_coffee**](#post_api_v1_roaster_roasterid_coffee) | **post** /api/v1/roaster/{roasterId}/coffee | 
[**put_api_v1_roaster_roasterid**](#put_api_v1_roaster_roasterid) | **put** /api/v1/roaster/{roasterId} | 
[**put_api_v1_roaster_roasterid_coffee_coffeeid**](#put_api_v1_roaster_roasterid_coffee_coffeeid) | **put** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 

# **delete_api_v1_roaster_roasterid**
<a name="delete_api_v1_roaster_roasterid"></a>
> delete_api_v1_roaster_roasterid(roaster_id)



Delete Roaster

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.delete_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->delete_api_v1_roaster_roasterid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    try:
        api_response = api_instance.delete_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->delete_api_v1_roaster_roasterid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_api_v1_roaster_roasterid.ApiResponseFor204) | 
400 | [ApiResponseFor400](#delete_api_v1_roaster_roasterid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#delete_api_v1_roaster_roasterid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#delete_api_v1_roaster_roasterid.ApiResponseFor404) | Resource not found
500 | [ApiResponseFor500](#delete_api_v1_roaster_roasterid.ApiResponseFor500) | Server error

#### delete_api_v1_roaster_roasterid.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_api_v1_roaster_roasterid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### delete_api_v1_roaster_roasterid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### delete_api_v1_roaster_roasterid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_api_v1_roaster_roasterid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="delete_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> delete_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_id)



Delete coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.delete_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->delete_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    try:
        api_response = api_instance.delete_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->delete_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 
coffeeId | CoffeeIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CoffeeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor204) | 
400 | [ApiResponseFor400](#delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404) | Resource not found
500 | [ApiResponseFor500](#delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500) | Server error

#### delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_account_logout**
<a name="get_api_v1_account_logout"></a>
> SuccessResult get_api_v1_account_logout()

Logout user

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only optional values
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
        'coffee_auth_refresh': "coffee_auth_refresh_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
        'X-Coffee-Refresh-Auth': "X-Coffee-Refresh-Auth_example",
    }
    try:
        # Logout user
        api_response = api_instance.get_api_v1_account_logout(
            header_params=header_params,
            cookie_params=cookie_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_account_logout: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
cookie_params | RequestCookieParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional
X-Coffee-Refresh-Auth | XCoffeeRefreshAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

# XCoffeeRefreshAuthSchema

Header used as re authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as re authentication header with JWT token | 

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional
coffee_auth_refresh | CoffeeAuthRefreshSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CoffeeAuthRefreshSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_account_logout.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_account_logout.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#get_api_v1_account_logout.ApiResponseFor401) | User session expired or user is not allowed to this resource
500 | [ApiResponseFor500](#get_api_v1_account_logout.ApiResponseFor500) | Server error

#### get_api_v1_account_logout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 


#### get_api_v1_account_logout.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_account_logout.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_api_v1_account_logout.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_account_register_verify**
<a name="get_api_v1_account_register_verify"></a>
> SuccessResult get_api_v1_account_register_verify(token)

Verify registration token and activate user account

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'token': "token_example",
    }
    header_params = {
    }
    try:
        # Verify registration token and activate user account
        api_response = api_instance.get_api_v1_account_register_verify(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_account_register_verify: %s\n" % e)

    # example passing only optional values
    query_params = {
        'token': "token_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        # Verify registration token and activate user account
        api_response = api_instance.get_api_v1_account_register_verify(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_account_register_verify: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
token | TokenSchema | | 


# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_account_register_verify.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_account_register_verify.ApiResponseFor400) | Content of request was logically invalid
500 | [ApiResponseFor500](#get_api_v1_account_register_verify.ApiResponseFor500) | Server error

#### get_api_v1_account_register_verify.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 


#### get_api_v1_account_register_verify.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_account_register_verify.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_coffee**
<a name="get_api_v1_coffee"></a>
> GetAllCoffeeResult get_api_v1_coffee()



Get all coffees

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.data_ordering import DataOrdering
from openapi_client.model.get_all_coffee_result import GetAllCoffeeResult
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.coffee_kind import CoffeeKind
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 10,
        'offset': 0,
        'kind': CoffeeKind("beans"),
        'created': DataOrdering("desc"),
        'updated': DataOrdering("desc"),
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        api_response = api_instance.get_api_v1_coffee(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_coffee: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
kind | KindSchema | | optional
created | CreatedSchema | | optional
updated | UpdatedSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# KindSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CoffeeKind**](../../models/CoffeeKind.md) |  | 


# CreatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


# UpdatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_coffee.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_coffee.ApiResponseFor400) | Content of request was logically invalid
500 | [ApiResponseFor500](#get_api_v1_coffee.ApiResponseFor500) | Server error

#### get_api_v1_coffee.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetAllCoffeeResult**](../../models/GetAllCoffeeResult.md) |  | 


#### get_api_v1_coffee.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_coffee.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_roaster**
<a name="get_api_v1_roaster"></a>
> GetAllRoasterResults get_api_v1_roaster()



Get all roaster entities from database

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.get_all_roaster_results import GetAllRoasterResults
from openapi_client.model.data_ordering import DataOrdering
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 10,
        'offset': 0,
        'created': DataOrdering("desc"),
        'updated': DataOrdering("desc"),
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        api_response = api_instance.get_api_v1_roaster(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
created | CreatedSchema | | optional
updated | UpdatedSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# CreatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


# UpdatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_roaster.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_roaster.ApiResponseFor400) | Content of request was logically invalid
500 | [ApiResponseFor500](#get_api_v1_roaster.ApiResponseFor500) | Server error

#### get_api_v1_roaster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetAllRoasterResults**](../../models/GetAllRoasterResults.md) |  | 


#### get_api_v1_roaster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_roaster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_roaster_roasterid**
<a name="get_api_v1_roaster_roasterid"></a>
> RoasterResult get_api_v1_roaster_roasterid(roaster_id)



Get roaster

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.roaster_result import RoasterResult
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    header_params = {
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_roaster_roasterid.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_roaster_roasterid.ApiResponseFor400) | Content of request was logically invalid
404 | [ApiResponseFor404](#get_api_v1_roaster_roasterid.ApiResponseFor404) | Resource not found
500 | [ApiResponseFor500](#get_api_v1_roaster_roasterid.ApiResponseFor500) | Server error

#### get_api_v1_roaster_roasterid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoasterResult**](../../models/RoasterResult.md) |  | 


#### get_api_v1_roaster_roasterid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_roaster_roasterid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_api_v1_roaster_roasterid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_roaster_roasterid_coffee**
<a name="get_api_v1_roaster_roasterid_coffee"></a>
> GetRoasterCoffeeResult get_api_v1_roaster_roasterid_coffee(roaster_id)



Get all roaster coffees

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.get_roaster_coffee_result import GetRoasterCoffeeResult
from openapi_client.model.not_found import NotFound
from openapi_client.model.data_ordering import DataOrdering
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.coffee_kind import CoffeeKind
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid_coffee(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid_coffee: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    query_params = {
        'limit': 10,
        'offset': 0,
        'kind': CoffeeKind("beans"),
        'created': DataOrdering("desc"),
        'updated': DataOrdering("desc"),
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid_coffee(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid_coffee: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
kind | KindSchema | | optional
created | CreatedSchema | | optional
updated | UpdatedSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# KindSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CoffeeKind**](../../models/CoffeeKind.md) |  | 


# CreatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


# UpdatedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataOrdering**](../../models/DataOrdering.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_roaster_roasterid_coffee.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_roaster_roasterid_coffee.ApiResponseFor400) | Content of request was logically invalid
404 | [ApiResponseFor404](#get_api_v1_roaster_roasterid_coffee.ApiResponseFor404) | Resource not found
500 | [ApiResponseFor500](#get_api_v1_roaster_roasterid_coffee.ApiResponseFor500) | Server error

#### get_api_v1_roaster_roasterid_coffee.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetRoasterCoffeeResult**](../../models/GetRoasterCoffeeResult.md) |  | 


#### get_api_v1_roaster_roasterid_coffee.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_roaster_roasterid_coffee.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_api_v1_roaster_roasterid_coffee.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="get_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> CoffeeResult get_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_id)



Get coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.coffee_result import CoffeeResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    header_params = {
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    try:
        api_response = api_instance.get_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->get_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 
coffeeId | CoffeeIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CoffeeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400) | Content of request was logically invalid
404 | [ApiResponseFor404](#get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404) | Resource not found
500 | [ApiResponseFor500](#get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500) | Server error

#### get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CoffeeResult**](../../models/CoffeeResult.md) |  | 


#### get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_api_v1_roaster_roasterid**
<a name="patch_api_v1_roaster_roasterid"></a>
> patch_api_v1_roaster_roasterid(roaster_idpatch_roaster_request)



Update Roaster field

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.patch_roaster_request import PatchRoasterRequest
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    body = PatchRoasterRequest(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.patch_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->patch_api_v1_roaster_roasterid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = PatchRoasterRequest(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.patch_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->patch_api_v1_roaster_roasterid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchRoasterRequest**](../../models/PatchRoasterRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#patch_api_v1_roaster_roasterid.ApiResponseFor204) | 
400 | [ApiResponseFor400](#patch_api_v1_roaster_roasterid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#patch_api_v1_roaster_roasterid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#patch_api_v1_roaster_roasterid.ApiResponseFor404) | Resource not found
422 | [ApiResponseFor422](#patch_api_v1_roaster_roasterid.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#patch_api_v1_roaster_roasterid.ApiResponseFor500) | Server error

#### patch_api_v1_roaster_roasterid.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor204 |  |
#### ResponseHeadersFor204

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### patch_api_v1_roaster_roasterid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_api_v1_roaster_roasterid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_api_v1_roaster_roasterid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_api_v1_roaster_roasterid.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### patch_api_v1_roaster_roasterid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="patch_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> patch_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_idpatch_coffee_request)



Update coffee field

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.patch_coffee_request import PatchCoffeeRequest
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    body = PatchCoffeeRequest(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.patch_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->patch_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = PatchCoffeeRequest(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.patch_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->patch_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchCoffeeRequest**](../../models/PatchCoffeeRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 
coffeeId | CoffeeIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CoffeeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor204) | 
400 | [ApiResponseFor400](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404) | Resource not found
422 | [ApiResponseFor422](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500) | Server error

#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor204 |  |
#### ResponseHeadersFor204

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### patch_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_login**
<a name="post_api_v1_account_login"></a>
> TokenResult post_api_v1_account_login(login_request)

Login user

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.token_result import TokenResult
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from openapi_client.model.login_request import LoginRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = LoginRequest(
        login="login_example",
        password="password_example",
    )
    try:
        # Login user
        api_response = api_instance.post_api_v1_account_login(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_login: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    body = LoginRequest(
        login="login_example",
        password="password_example",
    )
    try:
        # Login user
        api_response = api_instance.post_api_v1_account_login(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_login: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LoginRequest**](../../models/LoginRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_login.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_login.ApiResponseFor400) | Wrong login or password
422 | [ApiResponseFor422](#post_api_v1_account_login.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_account_login.ApiResponseFor500) | Server error

#### post_api_v1_account_login.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TokenResult**](../../models/TokenResult.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | 
X-Coffee-Refresh-Auth | XCoffeeRefreshAuthSchema | | 

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

# XCoffeeRefreshAuthSchema

Header used as re authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as re authentication header with JWT token | 


#### post_api_v1_account_login.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_account_login.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_account_login.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_password_reset**
<a name="post_api_v1_account_password_reset"></a>
> SuccessResult post_api_v1_account_password_reset(reset_password_input)

Send reset password link to user account

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.reset_password_input import ResetPasswordInput
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = ResetPasswordInput(
        login="login_example",
    )
    try:
        # Send reset password link to user account
        api_response = api_instance.post_api_v1_account_password_reset(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_password_reset: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    body = ResetPasswordInput(
        login="login_example",
    )
    try:
        # Send reset password link to user account
        api_response = api_instance.post_api_v1_account_password_reset(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_password_reset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResetPasswordInput**](../../models/ResetPasswordInput.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_password_reset.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_password_reset.ApiResponseFor400) | Content of request was logically invalid
422 | [ApiResponseFor422](#post_api_v1_account_password_reset.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_account_password_reset.ApiResponseFor500) | Server error

#### post_api_v1_account_password_reset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 


#### post_api_v1_account_password_reset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_account_password_reset.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_account_password_reset.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_password_reset_verify**
<a name="post_api_v1_account_password_reset_verify"></a>
> SuccessResult post_api_v1_account_password_reset_verify(change_password_request)

Verify user reset password token and change a password

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.change_password_request import ChangePasswordRequest
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = ChangePasswordRequest(
        token="token_example",
        password="password_example",
        repeat_password="repeat_password_example",
    )
    try:
        # Verify user reset password token and change a password
        api_response = api_instance.post_api_v1_account_password_reset_verify(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_password_reset_verify: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    body = ChangePasswordRequest(
        token="token_example",
        password="password_example",
        repeat_password="repeat_password_example",
    )
    try:
        # Verify user reset password token and change a password
        api_response = api_instance.post_api_v1_account_password_reset_verify(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_password_reset_verify: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ChangePasswordRequest**](../../models/ChangePasswordRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_password_reset_verify.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_password_reset_verify.ApiResponseFor400) | Content of request was logically invalid
422 | [ApiResponseFor422](#post_api_v1_account_password_reset_verify.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_account_password_reset_verify.ApiResponseFor500) | Server error

#### post_api_v1_account_password_reset_verify.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 


#### post_api_v1_account_password_reset_verify.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_account_password_reset_verify.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_account_password_reset_verify.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_register**
<a name="post_api_v1_account_register"></a>
> SuccessResult post_api_v1_account_register(registration_request)

Register new user and sends email to user for verification

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.registration_request import RegistrationRequest
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = RegistrationRequest(
        login="login_example",
        password="password_example",
        repeat_password="repeat_password_example",
    )
    try:
        # Register new user and sends email to user for verification
        api_response = api_instance.post_api_v1_account_register(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_register: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    body = RegistrationRequest(
        login="login_example",
        password="password_example",
        repeat_password="repeat_password_example",
    )
    try:
        # Register new user and sends email to user for verification
        api_response = api_instance.post_api_v1_account_register(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_register: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RegistrationRequest**](../../models/RegistrationRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_register.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_register.ApiResponseFor400) | Content of request was logically invalid
422 | [ApiResponseFor422](#post_api_v1_account_register.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_account_register.ApiResponseFor500) | Server error

#### post_api_v1_account_register.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 


#### post_api_v1_account_register.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_account_register.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_account_register.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_register_resend**
<a name="post_api_v1_account_register_resend"></a>
> SuccessResult post_api_v1_account_register_resend(registration_resend_request)

Creates new token and sends it to user

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.registration_resend_request import RegistrationResendRequest
from openapi_client.model.success_result import SuccessResult
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = RegistrationResendRequest(
        login="login_example",
    )
    try:
        # Creates new token and sends it to user
        api_response = api_instance.post_api_v1_account_register_resend(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_register_resend: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
    }
    body = RegistrationResendRequest(
        login="login_example",
    )
    try:
        # Creates new token and sends it to user
        api_response = api_instance.post_api_v1_account_register_resend(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_register_resend: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RegistrationResendRequest**](../../models/RegistrationResendRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_register_resend.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_register_resend.ApiResponseFor400) | Content of request was logically invalid
422 | [ApiResponseFor422](#post_api_v1_account_register_resend.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_account_register_resend.ApiResponseFor500) | Server error

#### post_api_v1_account_register_resend.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResult**](../../models/SuccessResult.md) |  | 


#### post_api_v1_account_register_resend.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_account_register_resend.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_account_register_resend.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_token_refresh**
<a name="post_api_v1_account_token_refresh"></a>
> TokenResult post_api_v1_account_token_refresh()

Refresh auth token

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.token_result import TokenResult
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only optional values
    cookie_params = {
        'coffee_auth_refresh': "coffee_auth_refresh_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Refresh-Auth': "X-Coffee-Refresh-Auth_example",
    }
    try:
        # Refresh auth token
        api_response = api_instance.post_api_v1_account_token_refresh(
            header_params=header_params,
            cookie_params=cookie_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_token_refresh: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
cookie_params | RequestCookieParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Refresh-Auth | XCoffeeRefreshAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeRefreshAuthSchema

Header used as re authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as re authentication header with JWT token | 

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth_refresh | CoffeeAuthRefreshSchema | | optional

# CoffeeAuthRefreshSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_token_refresh.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_token_refresh.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#post_api_v1_account_token_refresh.ApiResponseFor401) | User session expired or user is not allowed to this resource
500 | [ApiResponseFor500](#post_api_v1_account_token_refresh.ApiResponseFor500) | Server error

#### post_api_v1_account_token_refresh.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TokenResult**](../../models/TokenResult.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | 
X-Coffee-Refresh-Auth | XCoffeeRefreshAuthSchema | | 

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

# XCoffeeRefreshAuthSchema

Header used as re authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as re authentication header with JWT token | 


#### post_api_v1_account_token_refresh.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor400 |  |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 

#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 


#### post_api_v1_account_token_refresh.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor401 |  |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 

#### ResponseHeadersFor401

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 


#### post_api_v1_account_token_refresh.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Set-Cookie | SetCookieSchema | | optional

# SetCookieSchema

Cookie with re authentication JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cookie with re authentication JWT token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_account_token_verify**
<a name="post_api_v1_account_token_verify"></a>
> ValidTokenResult post_api_v1_account_token_verify()

Verify user session

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.invalid_token import InvalidToken
from openapi_client.model.valid_token_result import ValidTokenResult
from openapi_client.model.server_error import ServerError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only optional values
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    try:
        # Verify user session
        api_response = api_instance.post_api_v1_account_token_verify(
            header_params=header_params,
            cookie_params=cookie_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_account_token_verify: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
cookie_params | RequestCookieParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_api_v1_account_token_verify.ApiResponseFor200) | 
400 | [ApiResponseFor400](#post_api_v1_account_token_verify.ApiResponseFor400) | 
500 | [ApiResponseFor500](#post_api_v1_account_token_verify.ApiResponseFor500) | 

#### post_api_v1_account_token_verify.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidTokenResult**](../../models/ValidTokenResult.md) |  | 


#### post_api_v1_account_token_verify.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidToken**](../../models/InvalidToken.md) |  | 


#### post_api_v1_account_token_verify.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_roaster**
<a name="post_api_v1_roaster"></a>
> post_api_v1_roaster(roaster_request_entity)



Add Roaster

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.server_error import ServerError
from openapi_client.model.roaster_request_entity import RoasterRequestEntity
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    cookie_params = {
    }
    header_params = {
    }
    body = RoasterRequestEntity(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.post_api_v1_roaster(
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_roaster: %s\n" % e)

    # example passing only optional values
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = RoasterRequestEntity(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.post_api_v1_roaster(
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_roaster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoasterRequestEntity**](../../models/RoasterRequestEntity.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_api_v1_roaster.ApiResponseFor201) | 
400 | [ApiResponseFor400](#post_api_v1_roaster.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#post_api_v1_roaster.ApiResponseFor401) | User session expired or user is not allowed to this resource
422 | [ApiResponseFor422](#post_api_v1_roaster.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_roaster.ApiResponseFor500) | Server error

#### post_api_v1_roaster.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### post_api_v1_roaster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_roaster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### post_api_v1_roaster.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_roaster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_api_v1_roaster_roasterid_coffee**
<a name="post_api_v1_roaster_roasterid_coffee"></a>
> post_api_v1_roaster_roasterid_coffee(roaster_idcoffee_request_entity)



Add coffee to roaster

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from openapi_client.model.coffee_request_entity import CoffeeRequestEntity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    body = CoffeeRequestEntity(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.post_api_v1_roaster_roasterid_coffee(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_roaster_roasterid_coffee: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = CoffeeRequestEntity(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.post_api_v1_roaster_roasterid_coffee(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->post_api_v1_roaster_roasterid_coffee: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CoffeeRequestEntity**](../../models/CoffeeRequestEntity.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor201) | 
400 | [ApiResponseFor400](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor404) | Resource not found
422 | [ApiResponseFor422](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#post_api_v1_roaster_roasterid_coffee.ApiResponseFor500) | Server error

#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### post_api_v1_roaster_roasterid_coffee.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_api_v1_roaster_roasterid**
<a name="put_api_v1_roaster_roasterid"></a>
> put_api_v1_roaster_roasterid(roaster_idroaster_request_entity)



Update Roaster field

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.roaster_request_entity import RoasterRequestEntity
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    body = RoasterRequestEntity(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.put_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->put_api_v1_roaster_roasterid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = RoasterRequestEntity(
        name="name_example",
        full_name="full_name_example",
        country="country_example",
        city="city_example",
    )
    try:
        api_response = api_instance.put_api_v1_roaster_roasterid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->put_api_v1_roaster_roasterid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoasterRequestEntity**](../../models/RoasterRequestEntity.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#put_api_v1_roaster_roasterid.ApiResponseFor204) | 
400 | [ApiResponseFor400](#put_api_v1_roaster_roasterid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#put_api_v1_roaster_roasterid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#put_api_v1_roaster_roasterid.ApiResponseFor404) | Resource not found
422 | [ApiResponseFor422](#put_api_v1_roaster_roasterid.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#put_api_v1_roaster_roasterid.ApiResponseFor500) | Server error

#### put_api_v1_roaster_roasterid.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor204 |  |
#### ResponseHeadersFor204

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### put_api_v1_roaster_roasterid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### put_api_v1_roaster_roasterid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### put_api_v1_roaster_roasterid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### put_api_v1_roaster_roasterid.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### put_api_v1_roaster_roasterid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="put_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> put_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_idcoffee_request_entity)



Update coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import all_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.server_error import ServerError
from openapi_client.model.bad_request import BadRequest
from openapi_client.model.invalid_input import InvalidInput
from openapi_client.model.coffee_request_entity import CoffeeRequestEntity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_api.AllApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
    }
    header_params = {
    }
    body = CoffeeRequestEntity(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.put_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->put_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'roasterId': "roasterId_example",
        'coffeeId': "coffeeId_example",
    }
    cookie_params = {
        'coffee_auth': "coffee_auth_example",
    }
    header_params = {
        'X-Coffee-Request-ID': "X-Coffee-Request-ID_example",
        'X-Coffee-Auth': "X-Coffee-Auth_example",
    }
    body = CoffeeRequestEntity(
        name="name_example",
        grammage=Grammage(
            value=1,
            unit=UnitType("kg"),
        ),
        origin=[
            "origin_example"
        ],
        kind=CoffeeKind("beans"),
        beans=[
            Beans(
                kind=BeansKind("arabica"),
                ratio=3.14,
                varietal="varietal_example",
            )
        ],
        processing=[
            Processing("natural")
        ],
        roasting_level=1,
        dedicated=[
            BrewingMethod("espresso")
        ],
        description="description_example",
        speciality=True,
        roasting_dates=[
            "1970-01-01"
        ],
    )
    try:
        api_response = api_instance.put_api_v1_roaster_roasterid_coffee_coffeeid(
            path_params=path_params,
            header_params=header_params,
            cookie_params=cookie_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AllApi->put_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
cookie_params | RequestCookieParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CoffeeRequestEntity**](../../models/CoffeeRequestEntity.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Coffee-Request-ID | XCoffeeRequestIDSchema | | optional
X-Coffee-Auth | XCoffeeAuthSchema | | optional

# XCoffeeRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XCoffeeAuthSchema

Header used as authentication header with JWT token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Header used as authentication header with JWT token | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
roasterId | RoasterIdSchema | | 
coffeeId | CoffeeIdSchema | | 

# RoasterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# CoffeeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### cookie_params
#### RequestCookieParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
coffee_auth | CoffeeAuthSchema | | optional

# CoffeeAuthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor201) | 
400 | [ApiResponseFor400](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400) | Content of request was logically invalid
401 | [ApiResponseFor401](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401) | User session expired or user is not allowed to this resource
404 | [ApiResponseFor404](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404) | Resource not found
422 | [ApiResponseFor422](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor422) | Input request was invalid
500 | [ApiResponseFor500](#put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500) | Server error

#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | 

# LocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInput**](../../models/InvalidInput.md) |  | 


#### put_api_v1_roaster_roasterid_coffee_coffeeid.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerError**](../../models/ServerError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

