from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.bad_request import BadRequest
from ...models.data_ordering import DataOrdering
from ...models.coffee_kind import CoffeeKind
from typing import Union
from typing import Dict
from ...models.get_all_coffee_result import GetAllCoffeeResult
from ...models.server_error import ServerError
from ...types import UNSET, Unset
from typing import Optional



def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    kind: Union[Unset, None, CoffeeKind] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    updated: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/coffee".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id



    

    params: Dict[str, Any] = {}
    params["limit"] = limit


    params["offset"] = offset


    json_kind: Union[Unset, None, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value if kind else None

    params["kind"] = json_kind


    json_created: Union[Unset, None, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.value if created else None

    params["created"] = json_created


    json_updated: Union[Unset, None, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.value if updated else None

    params["updated"] = json_updated



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAllCoffeeResult.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    kind: Union[Unset, None, CoffeeKind] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    updated: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    """  Get all coffees

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        kind (Union[Unset, None, CoffeeKind]): Beans, grind coffee, capsules or instant
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        updated (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetAllCoffeeResult, ServerError]]
     """


    kwargs = _get_kwargs(
        client=client,
limit=limit,
offset=offset,
kind=kind,
created=created,
updated=updated,
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
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    kind: Union[Unset, None, CoffeeKind] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    updated: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    """  Get all coffees

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        kind (Union[Unset, None, CoffeeKind]): Beans, grind coffee, capsules or instant
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        updated (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetAllCoffeeResult, ServerError]
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,
kind=kind,
created=created,
updated=updated,
x_coffee_request_id=x_coffee_request_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    kind: Union[Unset, None, CoffeeKind] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    updated: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    """  Get all coffees

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        kind (Union[Unset, None, CoffeeKind]): Beans, grind coffee, capsules or instant
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        updated (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetAllCoffeeResult, ServerError]]
     """


    kwargs = _get_kwargs(
        client=client,
limit=limit,
offset=offset,
kind=kind,
created=created,
updated=updated,
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
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    kind: Union[Unset, None, CoffeeKind] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    updated: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, GetAllCoffeeResult, ServerError]]:
    """  Get all coffees

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        kind (Union[Unset, None, CoffeeKind]): Beans, grind coffee, capsules or instant
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        updated (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetAllCoffeeResult, ServerError]
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,
kind=kind,
created=created,
updated=updated,
x_coffee_request_id=x_coffee_request_id,

    )).parsed
