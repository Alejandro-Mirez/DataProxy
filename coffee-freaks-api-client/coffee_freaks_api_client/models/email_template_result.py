from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.email_content_type import EmailContentType
from ..models.email_template_type import EmailTemplateType






T = TypeVar("T", bound="EmailTemplateResult")


@attr.s(auto_attribs=True)
class EmailTemplateResult:
    """ 
        Attributes:
            template_type (EmailTemplateType): Email template type
            subject_template (str): What is email subject template
            content_template (str): What is email content template
            content_type (EmailContentType): Filter by email content type
            created (str): When template was created
            updated (str): Last update time of template
     """

    template_type: EmailTemplateType
    subject_template: str
    content_template: str
    content_type: EmailContentType
    created: str
    updated: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        template_type = self.template_type.value

        subject_template = self.subject_template
        content_template = self.content_template
        content_type = self.content_type.value

        created = self.created
        updated = self.updated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "templateType": template_type,
            "subjectTemplate": subject_template,
            "contentTemplate": content_template,
            "contentType": content_type,
            "created": created,
            "updated": updated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_type = EmailTemplateType(d.pop("templateType"))




        subject_template = d.pop("subjectTemplate")

        content_template = d.pop("contentTemplate")

        content_type = EmailContentType(d.pop("contentType"))




        created = d.pop("created")

        updated = d.pop("updated")

        email_template_result = cls(
            template_type=template_type,
            subject_template=subject_template,
            content_template=content_template,
            content_type=content_type,
            created=created,
            updated=updated,
        )

        email_template_result.additional_properties = d
        return email_template_result

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
