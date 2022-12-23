from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.brewing_method import BrewingMethod
from typing import cast, List
from typing import Dict
from typing import cast
from ..types import UNSET, Unset
from ..models.coffee_kind import CoffeeKind
from typing import Union
from ..models.processing import Processing
from dateutil.parser import isoparse
import datetime

if TYPE_CHECKING:
  from ..models.beans import Beans
  from ..models.grammage import Grammage




T = TypeVar("T", bound="CoffeeResult")

@attr.s(auto_attribs=True)
class CoffeeResult:
    """
    Attributes:
        id (str): Id of coffee
        roaster_id (str): To what roaster coffee belongs
        name (str): Name of coffee
        grammage (Grammage): How big package of coffee
        kind (CoffeeKind): Beans, grind coffee, capsules or instant
        speciality (bool): Rated as speciality coffee by roaster
        created (str): When it was created
        updated (str): When it was updated
        origin (Union[Unset, List[str]]): Where coffee beans comes from
        beans (Union[Unset, List['Beans']]): From where coffee comes from (Arabica, Robusta etc.) and in what ratio
        processing (Union[Unset, List[Processing]]): How coffee was processed (Honey, Natural etc.)
        roasting_level (Union[Unset, int]): Roasting level of beans - 2: Blond, 5: Medium, 8: Dark
        dedicated (Union[Unset, List[BrewingMethod]]): Dedicated to what type of brewing
        description (Union[Unset, str]): Description of product
        roasting_dates (Union[Unset, List[datetime.date]]): When coffee was roasted
    """

    id: str
    roaster_id: str
    name: str
    grammage: 'Grammage'
    kind: CoffeeKind
    speciality: bool
    created: str
    updated: str
    origin: Union[Unset, List[str]] = UNSET
    beans: Union[Unset, List['Beans']] = UNSET
    processing: Union[Unset, List[Processing]] = UNSET
    roasting_level: Union[Unset, int] = UNSET
    dedicated: Union[Unset, List[BrewingMethod]] = UNSET
    description: Union[Unset, str] = UNSET
    roasting_dates: Union[Unset, List[datetime.date]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.beans import Beans
        from ..models.grammage import Grammage
        id = self.id
        roaster_id = self.roaster_id
        name = self.name
        grammage = self.grammage.to_dict()

        kind = self.kind.value

        speciality = self.speciality
        created = self.created
        updated = self.updated
        origin: Union[Unset, List[str]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin




        beans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.beans, Unset):
            beans = []
            for beans_item_data in self.beans:
                beans_item = beans_item_data.to_dict()

                beans.append(beans_item)




        processing: Union[Unset, List[str]] = UNSET
        if not isinstance(self.processing, Unset):
            processing = []
            for processing_item_data in self.processing:
                processing_item = processing_item_data.value

                processing.append(processing_item)




        roasting_level = self.roasting_level
        dedicated: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dedicated, Unset):
            dedicated = []
            for dedicated_item_data in self.dedicated:
                dedicated_item = dedicated_item_data.value

                dedicated.append(dedicated_item)




        description = self.description
        roasting_dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.roasting_dates, Unset):
            roasting_dates = []
            for roasting_dates_item_data in self.roasting_dates:
                roasting_dates_item = roasting_dates_item_data.isoformat() 
                roasting_dates.append(roasting_dates_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "roasterId": roaster_id,
            "name": name,
            "grammage": grammage,
            "kind": kind,
            "speciality": speciality,
            "created": created,
            "updated": updated,
        })
        if origin is not UNSET:
            field_dict["origin"] = origin
        if beans is not UNSET:
            field_dict["beans"] = beans
        if processing is not UNSET:
            field_dict["processing"] = processing
        if roasting_level is not UNSET:
            field_dict["roastingLevel"] = roasting_level
        if dedicated is not UNSET:
            field_dict["dedicated"] = dedicated
        if description is not UNSET:
            field_dict["description"] = description
        if roasting_dates is not UNSET:
            field_dict["roastingDates"] = roasting_dates

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.beans import Beans
        from ..models.grammage import Grammage
        d = src_dict.copy()
        id = d.pop("id")

        roaster_id = d.pop("roasterId")

        name = d.pop("name")

        grammage = Grammage.from_dict(d.pop("grammage"))




        kind = CoffeeKind(d.pop("kind"))




        speciality = d.pop("speciality")

        created = d.pop("created")

        updated = d.pop("updated")

        origin = cast(List[str], d.pop("origin", UNSET))


        beans = []
        _beans = d.pop("beans", UNSET)
        for beans_item_data in (_beans or []):
            beans_item = Beans.from_dict(beans_item_data)



            beans.append(beans_item)


        processing = []
        _processing = d.pop("processing", UNSET)
        for processing_item_data in (_processing or []):
            processing_item = Processing(processing_item_data)



            processing.append(processing_item)


        roasting_level = d.pop("roastingLevel", UNSET)

        dedicated = []
        _dedicated = d.pop("dedicated", UNSET)
        for dedicated_item_data in (_dedicated or []):
            dedicated_item = BrewingMethod(dedicated_item_data)



            dedicated.append(dedicated_item)


        description = d.pop("description", UNSET)

        roasting_dates = []
        _roasting_dates = d.pop("roastingDates", UNSET)
        for roasting_dates_item_data in (_roasting_dates or []):
            roasting_dates_item = isoparse(roasting_dates_item_data).date()



            roasting_dates.append(roasting_dates_item)


        coffee_result = cls(
            id=id,
            roaster_id=roaster_id,
            name=name,
            grammage=grammage,
            kind=kind,
            speciality=speciality,
            created=created,
            updated=updated,
            origin=origin,
            beans=beans,
            processing=processing,
            roasting_level=roasting_level,
            dedicated=dedicated,
            description=description,
            roasting_dates=roasting_dates,
        )

        coffee_result.additional_properties = d
        return coffee_result

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
