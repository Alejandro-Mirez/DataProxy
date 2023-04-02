from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from ..models.email_status import EmailStatus
from ..models.email_content_type import EmailContentType
from typing import Union






T = TypeVar("T", bound="EmailResult")


@attr.s(auto_attribs=True)
class EmailResult:
    """ 
        Attributes:
            id (str): Email id
            recipient (str): Recipient to who email should be send
            subject (str): Subject of email
            content (str): Content of email
            content_type (EmailContentType): Filter by email content type
            created (str): When email was created
            next_try (str): When email will be retired
            tried (int): How many tries was preformed
            status (EmailStatus): Filter by email status
            last_try (Union[Unset, str]): When was last try
            send (Union[Unset, str]): When email was send
            message_id (Union[Unset, str]): What was message send it
            error (Union[Unset, str]): Error in case email was not send properly
     """

    id: str
    recipient: str
    subject: str
    content: str
    content_type: EmailContentType
    created: str
    next_try: str
    tried: int
    status: EmailStatus
    last_try: Union[Unset, str] = UNSET
    send: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        recipient = self.recipient
        subject = self.subject
        content = self.content
        content_type = self.content_type.value

        created = self.created
        next_try = self.next_try
        tried = self.tried
        status = self.status.value

        last_try = self.last_try
        send = self.send
        message_id = self.message_id
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "recipient": recipient,
            "subject": subject,
            "content": content,
            "contentType": content_type,
            "created": created,
            "nextTry": next_try,
            "tried": tried,
            "status": status,
        })
        if last_try is not UNSET:
            field_dict["lastTry"] = last_try
        if send is not UNSET:
            field_dict["send"] = send
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        recipient = d.pop("recipient")

        subject = d.pop("subject")

        content = d.pop("content")

        content_type = EmailContentType(d.pop("contentType"))




        created = d.pop("created")

        next_try = d.pop("nextTry")

        tried = d.pop("tried")

        status = EmailStatus(d.pop("status"))




        last_try = d.pop("lastTry", UNSET)

        send = d.pop("send", UNSET)

        message_id = d.pop("messageId", UNSET)

        error = d.pop("error", UNSET)

        email_result = cls(
            id=id,
            recipient=recipient,
            subject=subject,
            content=content,
            content_type=content_type,
            created=created,
            next_try=next_try,
            tried=tried,
            status=status,
            last_try=last_try,
            send=send,
            message_id=message_id,
            error=error,
        )

        email_result.additional_properties = d
        return email_result

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
