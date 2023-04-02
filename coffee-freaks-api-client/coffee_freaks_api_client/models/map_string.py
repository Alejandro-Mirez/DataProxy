from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset







T = TypeVar("T", bound="MapString")


@attr.s(auto_attribs=True)
class MapString:
    """ Meta information about validation result

     """

    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        map_string = cls(
        )


        map_string.additional_properties = d
        return map_string

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
