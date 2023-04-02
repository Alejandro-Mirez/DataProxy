from enum import Enum

class SimpleResultStatus(str, Enum):
    FAILURE = "Failure"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
