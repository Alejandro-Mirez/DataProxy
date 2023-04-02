from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.data_ordering import DataOrdering
from ..types import UNSET, Unset
from ..models.email_status import EmailStatus
from ..models.email_content_type import EmailContentType
from typing import Union






T = TypeVar("T", bound="GetAllEmailsParameters")


@attr.s(auto_attribs=True)
class GetAllEmailsParameters:
    """ Parameters used in query

        Attributes:
            limit (Union[Unset, int]): How many results should be returned per page. Default 10 Default: 10.
            offset (Union[Unset, int]): How many results should be removed from start of list
            recipient (Union[Unset, str]): Filter by recipient
            status (Union[Unset, EmailStatus]): Filter by email status
            content_type (Union[Unset, EmailContentType]): Filter by email content type
            created (Union[Unset, DataOrdering]): Sort by created field - default is DESC Default: DataOrdering.DESC.
     """

    limit: Union[Unset, int] = 10
    offset: Union[Unset, int] = 0
    recipient: Union[Unset, str] = UNSET
    status: Union[Unset, EmailStatus] = UNSET
    content_type: Union[Unset, EmailContentType] = UNSET
    created: Union[Unset, DataOrdering] = DataOrdering.DESC
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit
        offset = self.offset
        recipient = self.recipient
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if status is not UNSET:
            field_dict["status"] = status
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        recipient = d.pop("recipient", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EmailStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = EmailStatus(_status)




        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, EmailContentType]
        if isinstance(_content_type,  Unset):
            content_type = UNSET
        else:
            content_type = EmailContentType(_content_type)




        _created = d.pop("created", UNSET)
        created: Union[Unset, DataOrdering]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = DataOrdering(_created)




        get_all_emails_parameters = cls(
            limit=limit,
            offset=offset,
            recipient=recipient,
            status=status,
            content_type=content_type,
            created=created,
        )

        get_all_emails_parameters.additional_properties = d
        return get_all_emails_parameters

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
