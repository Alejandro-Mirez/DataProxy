from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.bad_request import BadRequest
from ...models.not_found import NotFound
from typing import Dict
from ...models.unauthorized import Unauthorized
from ...models.server_error import ServerError
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    roaster_id: str,
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/roaster/{roasterId}".format(
        client.base_url,roasterId=roaster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id

    if not isinstance(x_coffee_auth, Unset):
        headers["X-Coffee-Auth"] = x_coffee_auth



    if coffee_auth is not UNSET:
        cookies["coffee_auth"] = coffee_auth


    

    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.from_dict(response.json())



        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    roaster_id: str,
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """  Delete Roaster

    Args:
        roaster_id (str):
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        roaster_id=roaster_id,
client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    roaster_id: str,
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """  Delete Roaster

    Args:
        roaster_id (str):
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, NotFound, ServerError, Unauthorized]
     """


    return sync_detailed(
        roaster_id=roaster_id,
client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    ).parsed

async def asyncio_detailed(
    roaster_id: str,
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """  Delete Roaster

    Args:
        roaster_id (str):
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        roaster_id=roaster_id,
client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    roaster_id: str,
    *,
    client: Client,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """  Delete Roaster

    Args:
        roaster_id (str):
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, NotFound, ServerError, Unauthorized]
     """


    return (await asyncio_detailed(
        roaster_id=roaster_id,
client=client,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    )).parsed
