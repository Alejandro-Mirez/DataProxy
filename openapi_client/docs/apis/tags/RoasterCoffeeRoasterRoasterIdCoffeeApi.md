<a name="__pageTop"></a>
# openapi_client.apis.tags.roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v1_roaster_roasterid_coffee_coffeeid**](#delete_api_v1_roaster_roasterid_coffee_coffeeid) | **delete** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**get_api_v1_roaster_roasterid_coffee_coffeeid**](#get_api_v1_roaster_roasterid_coffee_coffeeid) | **get** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**patch_api_v1_roaster_roasterid_coffee_coffeeid**](#patch_api_v1_roaster_roasterid_coffee_coffeeid) | **patch** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 
[**post_api_v1_roaster_roasterid_coffee**](#post_api_v1_roaster_roasterid_coffee) | **post** /api/v1/roaster/{roasterId}/coffee | 
[**put_api_v1_roaster_roasterid_coffee_coffeeid**](#put_api_v1_roaster_roasterid_coffee_coffeeid) | **put** /api/v1/roaster/{roasterId}/coffee/{coffeeId} | 

# **delete_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="delete_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> delete_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_id)



Delete coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
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
    api_instance = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(api_client)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->delete_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->delete_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
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

# **get_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="get_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> CoffeeResult get_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_id)



Get coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
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
    api_instance = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(api_client)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->get_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->get_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
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

# **patch_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="patch_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> patch_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_idpatch_coffee_request)



Update coffee field

### Example

```python
import openapi_client
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
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
    api_instance = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(api_client)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->patch_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->patch_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
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

# **post_api_v1_roaster_roasterid_coffee**
<a name="post_api_v1_roaster_roasterid_coffee"></a>
> post_api_v1_roaster_roasterid_coffee(roaster_idcoffee_request_entity)



Add coffee to roaster

### Example

```python
import openapi_client
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
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
    api_instance = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(api_client)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->post_api_v1_roaster_roasterid_coffee: %s\n" % e)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->post_api_v1_roaster_roasterid_coffee: %s\n" % e)
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

# **put_api_v1_roaster_roasterid_coffee_coffeeid**
<a name="put_api_v1_roaster_roasterid_coffee_coffeeid"></a>
> put_api_v1_roaster_roasterid_coffee_coffeeid(roaster_idcoffee_idcoffee_request_entity)



Update coffee

### Example

```python
import openapi_client
from openapi_client.apis.tags import roaster_coffee_roaster_roaster_id_coffee_api
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
    api_instance = roaster_coffee_roaster_roaster_id_coffee_api.RoasterCoffeeRoasterRoasterIdCoffeeApi(api_client)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->put_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)

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
        print("Exception when calling RoasterCoffeeRoasterRoasterIdCoffeeApi->put_api_v1_roaster_roasterid_coffee_coffeeid: %s\n" % e)
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

