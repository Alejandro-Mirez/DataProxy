from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset






T = TypeVar("T", bound="RegistrationRequest")

@attr.s(auto_attribs=True)
class RegistrationRequest:
    """
    Attributes:
        login (str): Login must be an email
        password (str): Password at lest 8 symbols long with big and small letters, number and symbols
        repeat_password (str): Repeated password - needs to be same as original password
    """

    login: str
    password: str
    repeat_password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        password = self.password
        repeat_password = self.repeat_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "login": login,
            "password": password,
            "repeatPassword": repeat_password,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        password = d.pop("password")

        repeat_password = d.pop("repeatPassword")

        registration_request = cls(
            login=login,
            password=password,
            repeat_password=repeat_password,
        )

        registration_request.additional_properties = d
        return registration_request

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
