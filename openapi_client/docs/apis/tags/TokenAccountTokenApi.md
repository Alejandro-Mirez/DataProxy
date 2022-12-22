<a name="__pageTop"></a>
# openapi_client.apis.tags.token_account_token_api.TokenAccountTokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_api_v1_account_token_refresh**](#post_api_v1_account_token_refresh) | **post** /api/v1/account/token/refresh | Refresh auth token
[**post_api_v1_account_token_verify**](#post_api_v1_account_token_verify) | **post** /api/v1/account/token/verify | Verify user session

# **post_api_v1_account_token_refresh**
<a name="post_api_v1_account_token_refresh"></a>
> TokenResult post_api_v1_account_token_refresh()

Refresh auth token

### Example

```python
import openapi_client
from openapi_client.apis.tags import token_account_token_api
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
    api_instance = token_account_token_api.TokenAccountTokenApi(api_client)

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
        print("Exception when calling TokenAccountTokenApi->post_api_v1_account_token_refresh: %s\n" % e)
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
from openapi_client.apis.tags import token_account_token_api
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
    api_instance = token_account_token_api.TokenAccountTokenApi(api_client)

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
        print("Exception when calling TokenAccountTokenApi->post_api_v1_account_token_verify: %s\n" % e)
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

