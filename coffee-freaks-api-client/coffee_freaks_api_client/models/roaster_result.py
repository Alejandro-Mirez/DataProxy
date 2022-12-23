from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="RoasterResult")

@attr.s(auto_attribs=True)
class RoasterResult:
    """
    Attributes:
        id (str): Roaster id
        name (str): Label name of roaster
        full_name (str): Full name of roaster
        created (str): When it was created
        updated (str): When was updated
        country (Union[Unset, str]): From what country roaster origin
        city (Union[Unset, str]): In what city roaster originate
    """

    id: str
    name: str
    full_name: str
    created: str
    updated: str
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        full_name = self.full_name
        created = self.created
        updated = self.updated
        country = self.country
        city = self.city

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "fullName": full_name,
            "created": created,
            "updated": updated,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        full_name = d.pop("fullName")

        created = d.pop("created")

        updated = d.pop("updated")

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        roaster_result = cls(
            id=id,
            name=name,
            full_name=full_name,
            created=created,
            updated=updated,
            country=country,
            city=city,
        )

        roaster_result.additional_properties = d
        return roaster_result

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
