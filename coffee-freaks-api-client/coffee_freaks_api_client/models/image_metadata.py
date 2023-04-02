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
  from ..models.image_tag import ImageTag





T = TypeVar("T", bound="ImageMetadata")


@attr.s(auto_attribs=True)
class ImageMetadata:
    """ 
        Attributes:
            size_in_bytes (int):
            width (int):
            height (int):
            hash_ (str):
            format_ (str):
            tags (Union[Unset, List['ImageTag']]):
     """

    size_in_bytes: int
    width: int
    height: int
    hash_: str
    format_: str
    tags: Union[Unset, List['ImageTag']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.image_tag import ImageTag
        size_in_bytes = self.size_in_bytes
        width = self.width
        height = self.height
        hash_ = self.hash_
        format_ = self.format_
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sizeInBytes": size_in_bytes,
            "width": width,
            "height": height,
            "hash": hash_,
            "format": format_,
        })
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_tag import ImageTag
        d = src_dict.copy()
        size_in_bytes = d.pop("sizeInBytes")

        width = d.pop("width")

        height = d.pop("height")

        hash_ = d.pop("hash")

        format_ = d.pop("format")

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in (_tags or []):
            tags_item = ImageTag.from_dict(tags_item_data)



            tags.append(tags_item)


        image_metadata = cls(
            size_in_bytes=size_in_bytes,
            width=width,
            height=height,
            hash_=hash_,
            format_=format_,
            tags=tags,
        )

        image_metadata.additional_properties = d
        return image_metadata

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
