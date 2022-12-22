# coding: utf-8

"""
    Coffee Freaks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1-178-83b5c11-SNAPSHOT
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class MapString(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Meta information about validation result
    """


    class MetaOapg:
        additional_properties = schemas.StrSchema
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
    ) -> 'MapString':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
