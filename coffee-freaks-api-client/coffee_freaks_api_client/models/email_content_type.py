from enum import Enum

class EmailContentType(str, Enum):
    HTML = "HTML"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
