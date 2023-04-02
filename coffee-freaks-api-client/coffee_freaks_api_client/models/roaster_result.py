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
  from ..models.image_result import ImageResult





T = TypeVar("T", bound="RoasterResult")


@attr.s(auto_attribs=True)
class RoasterResult:
    """ 
        Attributes:
            id (str): Roaster id
            name (str): Label name of roaster
            full_address (str): Full address of roaster
            created (str): When it was created
            updated (str): When was updated
            country (Union[Unset, str]): From what country roaster origin
            city (Union[Unset, str]): In what city roaster originate
            images (Union[Unset, List['ImageResult']]): List of related images
     """

    id: str
    name: str
    full_address: str
    created: str
    updated: str
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    images: Union[Unset, List['ImageResult']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.image_result import ImageResult
        id = self.id
        name = self.name
        full_address = self.full_address
        created = self.created
        updated = self.updated
        country = self.country
        city = self.city
        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()

                images.append(images_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "fullAddress": full_address,
            "created": created,
            "updated": updated,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_result import ImageResult
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        full_address = d.pop("fullAddress")

        created = d.pop("created")

        updated = d.pop("updated")

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in (_images or []):
            images_item = ImageResult.from_dict(images_item_data)



            images.append(images_item)


        roaster_result = cls(
            id=id,
            name=name,
            full_address=full_address,
            created=created,
            updated=updated,
            country=country,
            city=city,
            images=images,
        )

        roaster_result.additional_properties = d
        return roaster_result

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
