from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.bad_request import BadRequest
from ...models.not_found import NotFound
from ...models.server_error import ServerError
from ...models.preview_template_request import PreviewTemplateRequest
from ...models.preview_result import PreviewResult
from typing import Dict
from ...models.unauthorized import Unauthorized
from ...models.invalid_input import InvalidInput
from ...models.email_template_type import EmailTemplateType
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    template_type: EmailTemplateType,
    *,
    client: Client,
    json_body: PreviewTemplateRequest,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/v1/email/template/{templateType}/preview".format(
        client.base_url,templateType=template_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_coffee_request_id, Unset):
        headers["X-Coffee-Request-ID"] = x_coffee_request_id

    if not isinstance(x_coffee_auth, Unset):
        headers["X-Coffee-Auth"] = x_coffee_auth



    if coffee_auth is not UNSET:
        cookies["coffee_auth"] = coffee_auth


    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PreviewResult.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.from_dict(response.json())



        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = InvalidInput.from_dict(response.json())



        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_type: EmailTemplateType,
    *,
    client: Client,
    json_body: PreviewTemplateRequest,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    """  Preview template

    Args:
        template_type (EmailTemplateType): Email template type
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        json_body (PreviewTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        template_type=template_type,
client=client,
json_body=json_body,
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
    template_type: EmailTemplateType,
    *,
    client: Client,
    json_body: PreviewTemplateRequest,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    """  Preview template

    Args:
        template_type (EmailTemplateType): Email template type
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        json_body (PreviewTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]
     """


    return sync_detailed(
        template_type=template_type,
client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    ).parsed

async def asyncio_detailed(
    template_type: EmailTemplateType,
    *,
    client: Client,
    json_body: PreviewTemplateRequest,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Response[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    """  Preview template

    Args:
        template_type (EmailTemplateType): Email template type
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        json_body (PreviewTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]
     """


    kwargs = _get_kwargs(
        template_type=template_type,
client=client,
json_body=json_body,
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
    template_type: EmailTemplateType,
    *,
    client: Client,
    json_body: PreviewTemplateRequest,
    x_coffee_request_id: Union[Unset, str] = UNSET,
    x_coffee_auth: Union[Unset, str] = UNSET,
    coffee_auth: Union[Unset, str] = UNSET,

) -> Optional[Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]]:
    """  Preview template

    Args:
        template_type (EmailTemplateType): Email template type
        x_coffee_request_id (Union[Unset, str]):
        x_coffee_auth (Union[Unset, str]):
        coffee_auth (Union[Unset, str]):
        json_body (PreviewTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, InvalidInput, NotFound, PreviewResult, ServerError, Unauthorized]
     """


    return (await asyncio_detailed(
        template_type=template_type,
client=client,
json_body=json_body,
x_coffee_request_id=x_coffee_request_id,
x_coffee_auth=x_coffee_auth,
coffee_auth=coffee_auth,

    )).parsed
