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
  from ..models.coffee_result import CoffeeResult
  from ..models.get_roaster_coffee_parameters import GetRoasterCoffeeParameters





T = TypeVar("T", bound="GetRoasterCoffeeResult")


@attr.s(auto_attribs=True)
class GetRoasterCoffeeResult:
    """ 
        Attributes:
            count (int): Count of all results
            parameters (GetRoasterCoffeeParameters): Parameters used in query
            results (Union[Unset, List['CoffeeResult']]): Results in actual page
     """

    count: int
    parameters: 'GetRoasterCoffeeParameters'
    results: Union[Unset, List['CoffeeResult']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.coffee_result import CoffeeResult
        from ..models.get_roaster_coffee_parameters import GetRoasterCoffeeParameters
        count = self.count
        parameters = self.parameters.to_dict()

        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "count": count,
            "parameters": parameters,
        })
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coffee_result import CoffeeResult
        from ..models.get_roaster_coffee_parameters import GetRoasterCoffeeParameters
        d = src_dict.copy()
        count = d.pop("count")

        parameters = GetRoasterCoffeeParameters.from_dict(d.pop("parameters"))




        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in (_results or []):
            results_item = CoffeeResult.from_dict(results_item_data)



            results.append(results_item)


        get_roaster_coffee_result = cls(
            count=count,
            parameters=parameters,
            results=results,
        )

        get_roaster_coffee_result.additional_properties = d
        return get_roaster_coffee_result

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
