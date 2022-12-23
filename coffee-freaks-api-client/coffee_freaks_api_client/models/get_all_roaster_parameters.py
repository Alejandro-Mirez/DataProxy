from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from ..models.data_ordering import DataOrdering





T = TypeVar("T", bound="GetAllRoasterParameters")

@attr.s(auto_attribs=True)
class GetAllRoasterParameters:
    """Parameters used in query

    Attributes:
        limit (int):
        offset (int):
        created (Union[Unset, DataOrdering]):  Default: DataOrdering.DESC.
        updated (Union[Unset, DataOrdering]):  Default: DataOrdering.DESC.
    """

    limit: int
    offset: int
    created: Union[Unset, DataOrdering] = DataOrdering.DESC
    updated: Union[Unset, DataOrdering] = DataOrdering.DESC
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit
        offset = self.offset
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




        get_all_roaster_parameters = cls(
            limit=limit,
            offset=offset,
            created=created,
            updated=updated,
        )

        get_all_roaster_parameters.additional_properties = d
        return get_all_roaster_parameters

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
