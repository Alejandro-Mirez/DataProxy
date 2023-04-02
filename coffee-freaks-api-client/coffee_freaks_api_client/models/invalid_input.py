from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from typing import cast, List
from typing import Dict
from ..types import UNSET, Unset
from typing import Union

if TYPE_CHECKING:
  from ..models.invalid_field import InvalidField





T = TypeVar("T", bound="InvalidInput")


@attr.s(auto_attribs=True)
class InvalidInput:
    """ 
        Attributes:
            message (str):
            fields (Union[Unset, List['InvalidField']]): List of invalid fields
     """

    message: str
    fields: Union[Unset, List['InvalidField']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invalid_field import InvalidField
        message = self.message
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
        })
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invalid_field import InvalidField
        d = src_dict.copy()
        message = d.pop("message")

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = InvalidField.from_dict(fields_item_data)



            fields.append(fields_item)


        invalid_input = cls(
            message=message,
            fields=fields,
        )

        invalid_input.additional_properties = d
        return invalid_input

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
