from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.bad_request import BadRequest
from ...models.success_result import SuccessResult
from ...models.unauthorized import Unauthorized
from typing import Dict
from ...models.server_error import ServerError
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    x_coffee_refresh_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth_refresh: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/account/logout".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id

    if not isinstance(x_coffee_auth, Unset):
        headers["X-Coffee-Auth"] = x_coffee_auth

    if not isinstance(x_coffee_refresh_auth, Unset):
        headers["X-Coffee-Refresh-Auth"] = x_coffee_refresh_auth



    if coffee_auth is not UNSET:
        cookies["coffee_auth"] = coffee_auth
    if coffee_auth_refresh is not UNSET:
        cookies["coffee_auth_refresh"] = coffee_auth_refresh


    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessResult.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    x_coffee_refresh_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth_refresh: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    """ Logout user

    Args:
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        x_coffee_refresh_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        coffee_auth_refresh (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]
     """


    kwargs = _get_kwargs(
        client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
x_coffee_refresh_auth=x_coffee_refresh_auth,
coffee_auth=coffee_auth,
coffee_auth_refresh=coffee_auth_refresh,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    x_coffee_refresh_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth_refresh: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    """ Logout user

    Args:
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        x_coffee_refresh_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        coffee_auth_refresh (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, ServerError, SuccessResult, Unauthorized]
     """


    return sync_detailed(
        client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
x_coffee_refresh_auth=x_coffee_refresh_auth,
coffee_auth=coffee_auth,
coffee_auth_refresh=coffee_auth_refresh,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    x_coffee_refresh_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth_refresh: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    """ Logout user

    Args:
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        x_coffee_refresh_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        coffee_auth_refresh (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]
     """


    kwargs = _get_kwargs(
        client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
x_coffee_refresh_auth=x_coffee_refresh_auth,
coffee_auth=coffee_auth,
coffee_auth_refresh=coffee_auth_refresh,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    x_coffee_refresh_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth_refresh: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, ServerError, SuccessResult, Unauthorized]]:
    """ Logout user

    Args:
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        x_coffee_refresh_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        coffee_auth_refresh (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, ServerError, SuccessResult, Unauthorized]
     """


    return (await asyncio_detailed(
        client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
x_coffee_refresh_auth=x_coffee_refresh_auth,
coffee_auth=coffee_auth,
coffee_auth_refresh=coffee_auth_refresh,

    )).parsed
