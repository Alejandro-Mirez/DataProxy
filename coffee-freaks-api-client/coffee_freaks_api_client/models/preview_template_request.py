from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.map_string import MapString





T = TypeVar("T", bound="PreviewTemplateRequest")


@attr.s(auto_attribs=True)
class PreviewTemplateRequest:
    """ 
        Attributes:
            subject_template (str):
            content_template (str):
            content_variables (Union[Unset, MapString]): Meta information about validation result
     """

    subject_template: str
    content_template: str
    content_variables: Union[Unset, 'MapString'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.map_string import MapString
        subject_template = self.subject_template
        content_template = self.content_template
        content_variables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_variables, Unset):
            content_variables = self.content_variables.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subjectTemplate": subject_template,
            "contentTemplate": content_template,
        })
        if content_variables is not UNSET:
            field_dict["contentVariables"] = content_variables

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_string import MapString
        d = src_dict.copy()
        subject_template = d.pop("subjectTemplate")

        content_template = d.pop("contentTemplate")

        _content_variables = d.pop("contentVariables", UNSET)
        content_variables: Union[Unset, MapString]
        if isinstance(_content_variables,  Unset):
            content_variables = UNSET
        else:
            content_variables = MapString.from_dict(_content_variables)




        preview_template_request = cls(
            subject_template=subject_template,
            content_template=content_template,
            content_variables=content_variables,
        )

        preview_template_request.additional_properties = d
        return preview_template_request

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
