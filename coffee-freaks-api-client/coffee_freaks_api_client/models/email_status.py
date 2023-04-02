from enum import Enum

class EmailStatus(str, Enum):
    FAILED_GENERATING_TEMPLATE = "FAILED_GENERATING_TEMPLATE"
    FAILED_TO_SEND = "FAILED_TO_SEND"
    QUEUED = "QUEUED"
    SEND = "SEND"

    def __str__(self) -> str:
        return str(self.value)
