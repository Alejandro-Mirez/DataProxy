<a name="__pageTop"></a>
# openapi_client.apis.tags.register_account_register_api.RegisterAccountRegisterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_account_register_verify**](#get_api_v1_account_register_verify) | **get** /api/v1/account/register/verify | Verify registration token and activate user account
[**post_api_v1_account_register**](#post_api_v1_account_register) | **post** /api/v1/account/register | Register new user and sends email to user for verification
[**post_api_v1_account_register_resend**](#post_api_v1_account_register_resend) | **post** /api/v1/account/register/resend | Creates new token and sends it to user

# **get_api_v1_account_register_verify**
<a name="get_api_v1_account_register_verify"></a>
> SuccessResult get_api_v1_account_register_verify(token)

Verify registration token and activate user account

### Example

```python
import openapi_client
from openapi_client.apis.tags import register_account_register_api
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
    api_instance = register_account_register_api.RegisterAccountRegisterApi(api_client)

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
        print("Exception when calling RegisterAccountRegisterApi->get_api_v1_account_register_verify: %s\n" % e)

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
        print("Exception when calling RegisterAccountRegisterApi->get_api_v1_account_register_verify: %s\n" % e)
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

# **post_api_v1_account_register**
<a name="post_api_v1_account_register"></a>
> SuccessResult post_api_v1_account_register(registration_request)

Register new user and sends email to user for verification

### Example

```python
import openapi_client
from openapi_client.apis.tags import register_account_register_api
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
    api_instance = register_account_register_api.RegisterAccountRegisterApi(api_client)

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
        print("Exception when calling RegisterAccountRegisterApi->post_api_v1_account_register: %s\n" % e)

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
        print("Exception when calling RegisterAccountRegisterApi->post_api_v1_account_register: %s\n" % e)
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
from openapi_client.apis.tags import register_account_register_api
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
    api_instance = register_account_register_api.RegisterAccountRegisterApi(api_client)

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
        print("Exception when calling RegisterAccountRegisterApi->post_api_v1_account_register_resend: %s\n" % e)

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
        print("Exception when calling RegisterAccountRegisterApi->post_api_v1_account_register_resend: %s\n" % e)
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

