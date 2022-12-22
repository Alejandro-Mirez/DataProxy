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


class Beans(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "kind",
            "ratio",
        }
        
        class properties:
        
            @staticmethod
            def kind() -> typing.Type['BeansKind']:
                return BeansKind
            ratio = schemas.Float64Schema
            varietal = schemas.StrSchema
            __annotations__ = {
                "kind": kind,
                "ratio": ratio,
                "varietal": varietal,
            }
    
    kind: 'BeansKind'
    ratio: MetaOapg.properties.ratio
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> 'BeansKind': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratio"]) -> MetaOapg.properties.ratio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["varietal"]) -> MetaOapg.properties.varietal: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["kind", "ratio", "varietal", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> 'BeansKind': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratio"]) -> MetaOapg.properties.ratio: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["varietal"]) -> typing.Union[MetaOapg.properties.varietal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["kind", "ratio", "varietal", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        kind: 'BeansKind',
        ratio: typing.Union[MetaOapg.properties.ratio, decimal.Decimal, int, float, ],
        varietal: typing.Union[MetaOapg.properties.varietal, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Beans':
        return super().__new__(
            cls,
            *args,
            kind=kind,
            ratio=ratio,
            varietal=varietal,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.beans_kind import BeansKind
