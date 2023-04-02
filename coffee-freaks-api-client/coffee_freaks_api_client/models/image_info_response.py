from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.image_metadata import ImageMetadata





T = TypeVar("T", bound="ImageInfoResponse")


@attr.s(auto_attribs=True)
class ImageInfoResponse:
    """ 
        Attributes:
            filename (str):
            owner (str):
            owner_id (str):
            metadata (ImageMetadata):
            created (str):
            updated (str):
            store_path (Union[Unset, str]):
            store_type (Union[Unset, str]):
            category (Union[Unset, str]):
     """

    filename: str
    owner: str
    owner_id: str
    metadata: 'ImageMetadata'
    created: str
    updated: str
    store_path: Union[Unset, str] = UNSET
    store_type: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.image_metadata import ImageMetadata
        filename = self.filename
        owner = self.owner
        owner_id = self.owner_id
        metadata = self.metadata.to_dict()

        created = self.created
        updated = self.updated
        store_path = self.store_path
        store_type = self.store_type
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "filename": filename,
            "owner": owner,
            "ownerId": owner_id,
            "metadata": metadata,
            "created": created,
            "updated": updated,
        })
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_metadata import ImageMetadata
        d = src_dict.copy()
        filename = d.pop("filename")

        owner = d.pop("owner")

        owner_id = d.pop("ownerId")

        metadata = ImageMetadata.from_dict(d.pop("metadata"))




        created = d.pop("created")

        updated = d.pop("updated")

        store_path = d.pop("storePath", UNSET)

        store_type = d.pop("storeType", UNSET)

        category = d.pop("category", UNSET)

        image_info_response = cls(
            filename=filename,
            owner=owner,
            owner_id=owner_id,
            metadata=metadata,
            created=created,
            updated=updated,
            store_path=store_path,
            store_type=store_type,
            category=category,
        )

        image_info_response.additional_properties = d
        return image_info_response

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
