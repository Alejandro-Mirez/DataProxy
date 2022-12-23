from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.server_error import ServerError
from typing import Dict
from typing import cast
from ...models.success_result import SuccessResult
from ...types import UNSET, Unset
from typing import Union
from ...models.bad_request import BadRequest



def _get_kwargs(
    *,
    client: Client,
    token: str,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/account/register/verify".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id



    

    params: Dict[str, Any] = {}
    params["token"] = token



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, ServerError, SuccessResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessResult.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, ServerError, SuccessResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    token: str,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, ServerError, SuccessResult]]:
    """Verify registration token and activate user account

    Args:
        token (str):
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult]]
    """


    kwargs = _get_kwargs(
        client=client,
token=token,
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
    token: str,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, ServerError, SuccessResult]]:
    """Verify registration token and activate user account

    Args:
        token (str):
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult]]
    """


    return sync_detailed(
        client=client,
token=token,
x_coffee_request_id=x_coffee_request_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    token: str,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, ServerError, SuccessResult]]:
    """Verify registration token and activate user account

    Args:
        token (str):
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult]]
    """


    kwargs = _get_kwargs(
        client=client,
token=token,
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
    token: str,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, ServerError, SuccessResult]]:
    """Verify registration token and activate user account

    Args:
        token (str):
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult]]
    """


    return (await asyncio_detailed(
        client=client,
token=token,
x_coffee_request_id=x_coffee_request_id,

    )).parsed

