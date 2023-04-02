from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset







T = TypeVar("T", bound="ImageTag")


@attr.s(auto_attribs=True)
class ImageTag:
    """ 
        Attributes:
            name (str):
            type (int):
            raw_value (str):
            value (str):
     """

    name: str
    type: int
    raw_value: str
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        raw_value = self.raw_value
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "type": type,
            "rawValue": raw_value,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = d.pop("type")

        raw_value = d.pop("rawValue")

        value = d.pop("value")

        image_tag = cls(
            name=name,
            type=type,
            raw_value=raw_value,
            value=value,
        )

        image_tag.additional_properties = d
        return image_tag

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
