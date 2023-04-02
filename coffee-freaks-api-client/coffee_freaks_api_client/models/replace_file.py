from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr
import json

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from ..types import File, FileJsonType
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="ReplaceFile")


@attr.s(auto_attribs=True)
class ReplaceFile:
    """ 
        Attributes:
            image (File):
            filename (str):
            category (Union[Unset, str]):
     """

    image: File
    filename: str
    category: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        image = self.image.to_tuple()

        filename = self.filename
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "image": image,
            "filename": filename,
        })
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict


    def to_multipart(self) -> Dict[str, Any]:
        image = self.image.to_tuple()

        filename = self.filename if isinstance(self.filename, Unset) else (None, str(self.filename).encode(), "text/plain")
        category = self.category if isinstance(self.category, Unset) else (None, str(self.category).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({
            key: (None, str(value).encode(), "text/plain")
            for key, value in self.additional_properties.items()
        })
        field_dict.update({
            "image": image,
            "filename": filename,
        })
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict


    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image = File(
             payload = BytesIO(d.pop("image"))
        )




        filename = d.pop("filename")

        category = d.pop("category", UNSET)

        replace_file = cls(
            image=image,
            filename=filename,
            category=category,
        )

        replace_file.additional_properties = d
        return replace_file

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
