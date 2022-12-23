from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="PatchRoasterRequest")

@attr.s(auto_attribs=True)
class PatchRoasterRequest:
    """
    Attributes:
        name (Union[Unset, str]): Label name of roaster
        full_name (Union[Unset, str]): Full name of roaster
        country (Union[Unset, str]): From what country roaster origin
        city (Union[Unset, str]): In what city roaster originate
    """

    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        full_name = self.full_name
        country = self.country
        city = self.city

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        patch_roaster_request = cls(
            name=name,
            full_name=full_name,
            country=country,
            city=city,
        )

        patch_roaster_request.additional_properties = d
        return patch_roaster_request

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
