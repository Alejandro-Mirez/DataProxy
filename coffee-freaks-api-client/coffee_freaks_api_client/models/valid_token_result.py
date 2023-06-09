from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset







T = TypeVar("T", bound="ValidTokenResult")


@attr.s(auto_attribs=True)
class ValidTokenResult:
    """ 
        Attributes:
            id (str): User id
            login (str): Account login used to login
            valid_to (str): DateTime with date till token is valid
     """

    id: str
    login: str
    valid_to: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        login = self.login
        valid_to = self.valid_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "login": login,
            "validTo": valid_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        login = d.pop("login")

        valid_to = d.pop("validTo")

        valid_token_result = cls(
            id=id,
            login=login,
            valid_to=valid_to,
        )

        valid_token_result.additional_properties = d
        return valid_token_result

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
