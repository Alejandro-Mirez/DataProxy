<a name="__pageTop"></a>
# openapi_client.apis.tags.password_account_password_api.PasswordAccountPasswordApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_api_v1_account_password_reset**](#post_api_v1_account_password_reset) | **post** /api/v1/account/password/reset | Send reset password link to user account
[**post_api_v1_account_password_reset_verify**](#post_api_v1_account_password_reset_verify) | **post** /api/v1/account/password/reset/verify | Verify user reset password token and change a password

# **post_api_v1_account_password_reset**
<a name="post_api_v1_account_password_reset"></a>
> SuccessResult post_api_v1_account_password_reset(reset_password_input)

Send reset password link to user account

### Example

```python
import openapi_client
from openapi_client.apis.tags import password_account_password_api
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
    api_instance = password_account_password_api.PasswordAccountPasswordApi(api_client)

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
        print("Exception when calling PasswordAccountPasswordApi->post_api_v1_account_password_reset: %s\n" % e)

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
        print("Exception when calling PasswordAccountPasswordApi->post_api_v1_account_password_reset: %s\n" % e)
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
from openapi_client.apis.tags import password_account_password_api
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
    api_instance = password_account_password_api.PasswordAccountPasswordApi(api_client)

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
        print("Exception when calling PasswordAccountPasswordApi->post_api_v1_account_password_reset_verify: %s\n" % e)

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
        print("Exception when calling PasswordAccountPasswordApi->post_api_v1_account_password_reset_verify: %s\n" % e)
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

