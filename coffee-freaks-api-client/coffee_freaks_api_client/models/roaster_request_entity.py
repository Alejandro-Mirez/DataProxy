from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RoasterRequestEntity")


@attr.s(auto_attribs=True)
class RoasterRequestEntity:
    """ 
        Attributes:
            name (str): Label name of roaster
            full_address (str): Full name of roaster
            country (Union[Unset, str]): From what country roaster origin
            city (Union[Unset, str]): In what city roaster originate
     """

    name: str
    full_address: str
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        full_address = self.full_address
        country = self.country
        city = self.city

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "fullAddress": full_address,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        full_address = d.pop("fullAddress")

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        roaster_request_entity = cls(
            name=name,
            full_address=full_address,
            country=country,
            city=city,
        )

        roaster_request_entity.additional_properties = d
        return roaster_request_entity

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
