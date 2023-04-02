from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from ..models.beans_kind import BeansKind
from typing import Union






T = TypeVar("T", bound="Beans")


@attr.s(auto_attribs=True)
class Beans:
    """ 
        Attributes:
            kind (BeansKind): Name of coffee
            ratio (float): Ratio. 1 is 100%, 0.5 is 50% etc.
            varietal (Union[Unset, str]): Bourbon, Caturra etc.
     """

    kind: BeansKind
    ratio: float
    varietal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        ratio = self.ratio
        varietal = self.varietal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "ratio": ratio,
        })
        if varietal is not UNSET:
            field_dict["varietal"] = varietal

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = BeansKind(d.pop("kind"))




        ratio = d.pop("ratio")

        varietal = d.pop("varietal", UNSET)

        beans = cls(
            kind=kind,
            ratio=ratio,
            varietal=varietal,
        )

        beans.additional_properties = d
        return beans

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
