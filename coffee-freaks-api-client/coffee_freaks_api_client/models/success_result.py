from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.simple_result_status import SimpleResultStatus
from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="SuccessResult")

@attr.s(auto_attribs=True)
class SuccessResult:
    """
    Attributes:
        status (SimpleResultStatus):
        message (Union[Unset, str]):
    """

    status: SimpleResultStatus
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = SimpleResultStatus(d.pop("status"))




        message = d.pop("message", UNSET)

        success_result = cls(
            status=status,
            message=message,
        )

        success_result.additional_properties = d
        return success_result

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
