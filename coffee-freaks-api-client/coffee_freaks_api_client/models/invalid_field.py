from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.map_string import MapString





T = TypeVar("T", bound="InvalidField")


@attr.s(auto_attribs=True)
class InvalidField:
    """ 
        Attributes:
            name (str): Name of the field that is invalid
            error (str): Description of error
            error_code (str): Text representation of error code
            meta (MapString): Meta information about validation result
     """

    name: str
    error: str
    error_code: str
    meta: 'MapString'
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.map_string import MapString
        name = self.name
        error = self.error
        error_code = self.error_code
        meta = self.meta.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "error": error,
            "errorCode": error_code,
            "meta": meta,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_string import MapString
        d = src_dict.copy()
        name = d.pop("name")

        error = d.pop("error")

        error_code = d.pop("errorCode")

        meta = MapString.from_dict(d.pop("meta"))




        invalid_field = cls(
            name=name,
            error=error,
            error_code=error_code,
            meta=meta,
        )

        invalid_field.additional_properties = d
        return invalid_field

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
