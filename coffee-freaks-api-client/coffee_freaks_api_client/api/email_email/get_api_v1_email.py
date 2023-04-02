from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.bad_request import BadRequest
from ...models.get_emails_response import GetEmailsResponse
from ...models.data_ordering import DataOrdering
from ...models.email_content_type import EmailContentType
from ...models.email_status import EmailStatus
from typing import Optional
from typing import Dict
from ...models.unauthorized import Unauthorized
from ...models.server_error import ServerError
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    recipient: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, EmailStatus] = UNSET,
    content_type: Union[Unset, None, EmailContentType] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/email".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id

    if not isinstance(x_coffee_auth, Unset):
        headers["X-Coffee-Auth"] = x_coffee_auth



    if coffee_auth is not UNSET:
        cookies["coffee_auth"] = coffee_auth


    params: Dict[str, Any] = {}
    params["limit"] = limit


    params["offset"] = offset


    params["recipient"] = recipient


    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status


    json_content_type: Union[Unset, None, str] = UNSET
    if not isinstance(content_type, Unset):
        json_content_type = content_type.value if content_type else None

    params["contentType"] = json_content_type


    json_created: Union[Unset, None, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.value if created else None

    params["created"] = json_created



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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetEmailsResponse.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
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
    recipient: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, EmailStatus] = UNSET,
    content_type: Union[Unset, None, EmailContentType] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
    """  Get emails

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        recipient (Union[Unset, None, str]):
        status (Union[Unset, None, EmailStatus]): Filter by email status
        content_type (Union[Unset, None, EmailContentType]): Filter by email content type
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        client=client,
limit=limit,
offset=offset,
recipient=recipient,
status=status,
content_type=content_type,
created=created,
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
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    recipient: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, EmailStatus] = UNSET,
    content_type: Union[Unset, None, EmailContentType] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
    """  Get emails

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        recipient (Union[Unset, None, str]):
        status (Union[Unset, None, EmailStatus]): Filter by email status
        content_type (Union[Unset, None, EmailContentType]): Filter by email content type
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,
recipient=recipient,
status=status,
content_type=content_type,
created=created,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    recipient: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, EmailStatus] = UNSET,
    content_type: Union[Unset, None, EmailContentType] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
    """  Get emails

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        recipient (Union[Unset, None, str]):
        status (Union[Unset, None, EmailStatus]): Filter by email status
        content_type (Union[Unset, None, EmailContentType]): Filter by email content type
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        client=client,
limit=limit,
offset=offset,
recipient=recipient,
status=status,
content_type=content_type,
created=created,
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
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    recipient: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, EmailStatus] = UNSET,
    content_type: Union[Unset, None, EmailContentType] = UNSET,
    created: Union[Unset, None, DataOrdering] = DataOrdering.DESC,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]]:
    """  Get emails

    Args:
        limit (Union[Unset, None, int]): How many results should be returned per page. Default 10
            Default: 10.
        offset (Union[Unset, None, int]): How many results should be removed from start of list
        recipient (Union[Unset, None, str]):
        status (Union[Unset, None, EmailStatus]): Filter by email status
        content_type (Union[Unset, None, EmailContentType]): Filter by email content type
        created (Union[Unset, None, DataOrdering]): Sort by created field - default is DESC
            Default: DataOrdering.DESC.
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, GetEmailsResponse, ServerError, Unauthorized]
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,
recipient=recipient,
status=status,
content_type=content_type,
created=created,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    )).parsed
