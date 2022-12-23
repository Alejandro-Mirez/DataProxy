from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from ..models.coffee_kind import CoffeeKind
from ..models.data_ordering import DataOrdering





T = TypeVar("T", bound="GetAllCoffeeParameters")

@attr.s(auto_attribs=True)
class GetAllCoffeeParameters:
    """Parameters used in query

    Attributes:
        limit (int):
        offset (int):
        kind (Union[Unset, CoffeeKind]): Beans, grind coffee, capsules or instant
        created (Union[Unset, DataOrdering]):  Default: DataOrdering.DESC.
        updated (Union[Unset, DataOrdering]):  Default: DataOrdering.DESC.
    """

    limit: int
    offset: int
    kind: Union[Unset, CoffeeKind] = UNSET
    created: Union[Unset, DataOrdering] = DataOrdering.DESC
    updated: Union[Unset, DataOrdering] = DataOrdering.DESC
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit
        offset = self.offset
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.value

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "limit": limit,
            "offset": offset,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit")

        offset = d.pop("offset")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, CoffeeKind]
        if isinstance(_kind,  Unset) or _kind is None:
            kind = UNSET
        else:
            kind = CoffeeKind(_kind)




        _created = d.pop("created", UNSET)
        created: Union[Unset, DataOrdering]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = DataOrdering(_created)




        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, DataOrdering]
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = DataOrdering(_updated)




        get_all_coffee_parameters = cls(
            limit=limit,
            offset=offset,
            kind=kind,
            created=created,
            updated=updated,
        )

        get_all_coffee_parameters.additional_properties = d
        return get_all_coffee_parameters

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
