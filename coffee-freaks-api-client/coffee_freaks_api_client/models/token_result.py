from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset







T = TypeVar("T", bound="TokenResult")


@attr.s(auto_attribs=True)
class TokenResult:
    """ 
        Attributes:
            auth_token (str): Token used as auth token in X-Coffee-Auth header
            refresh_token (str): Token used as refresh token in X-Coffee-Refresh-Auth header
     """

    auth_token: str
    refresh_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        auth_token = self.auth_token
        refresh_token = self.refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authToken": auth_token,
            "refreshToken": refresh_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_token = d.pop("authToken")

        refresh_token = d.pop("refreshToken")

        token_result = cls(
            auth_token=auth_token,
            refresh_token=refresh_token,
        )

        token_result.additional_properties = d
        return token_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
