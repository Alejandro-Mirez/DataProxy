<a name="__pageTop"></a>
# openapi_client.apis.tags.coffee_coffee_api.CoffeeCoffeeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_coffee**](#get_api_v1_coffee) | **get** /api/v1/coffee | 

# **get_api_v1_coffee**
<a name="get_api_v1_coffee"></a>
> GetAllCoffeeResult get_api_v1_coffee()



Get all coffees

### Example

```python
import openapi_client
from openapi_client.apis.tags import coffee_coffee_api
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
    api_instance = coffee_coffee_api.CoffeeCoffeeApi(api_client)

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
        print("Exception when calling CoffeeCoffeeApi->get_api_v1_coffee: %s\n" % e)
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

