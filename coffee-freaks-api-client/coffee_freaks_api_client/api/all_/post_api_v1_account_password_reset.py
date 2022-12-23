from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_input import InvalidInput
from ...models.server_error import ServerError
from ...models.reset_password_input import ResetPasswordInput
from typing import Dict
from typing import cast
from ...models.success_result import SuccessResult
from ...types import UNSET, Unset
from typing import Union
from ...models.bad_request import BadRequest



def _get_kwargs(
    *,
    client: Client,
    json_body: ResetPasswordInput,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/account/password/reset".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id



    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessResult.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = InvalidInput.from_dict(response.json())



        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ResetPasswordInput,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    """Send reset password link to user account

    Args:
        x_coffee_request_id (Union[Unset, str]):
        json_body (ResetPasswordInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    json_body: ResetPasswordInput,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    """Send reset password link to user account

    Args:
        x_coffee_request_id (Union[Unset, str]):
        json_body (ResetPasswordInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]
    """


    return sync_detailed(
        client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: ResetPasswordInput,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    """Send reset password link to user account

    Args:
        x_coffee_request_id (Union[Unset, str]):
        json_body (ResetPasswordInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    json_body: ResetPasswordInput,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]:
    """Send reset password link to user account

    Args:
        x_coffee_request_id (Union[Unset, str]):
        json_body (ResetPasswordInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, ServerError, SuccessResult]]
    """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,

    )).parsed

