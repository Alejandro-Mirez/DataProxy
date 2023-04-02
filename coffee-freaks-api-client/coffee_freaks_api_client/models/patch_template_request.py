from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from ..models.email_content_type import EmailContentType
from typing import Union






T = TypeVar("T", bound="PatchTemplateRequest")


@attr.s(auto_attribs=True)
class PatchTemplateRequest:
    """ 
        Attributes:
            subject_template (Union[Unset, str]):
            content_template (Union[Unset, str]):
            content_type (Union[Unset, EmailContentType]): Filter by email content type
     """

    subject_template: Union[Unset, str] = UNSET
    content_template: Union[Unset, str] = UNSET
    content_type: Union[Unset, EmailContentType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject_template = self.subject_template
        content_template = self.content_template
        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if subject_template is not UNSET:
            field_dict["subjectTemplate"] = subject_template
        if content_template is not UNSET:
            field_dict["contentTemplate"] = content_template
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_template = d.pop("subjectTemplate", UNSET)

        content_template = d.pop("contentTemplate", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, EmailContentType]
        if isinstance(_content_type,  Unset):
            content_type = UNSET
        else:
            content_type = EmailContentType(_content_type)




        patch_template_request = cls(
            subject_template=subject_template,
            content_template=content_template,
            content_type=content_type,
        )

        patch_template_request.additional_properties = d
        return patch_template_request

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
