from enum import Enum

class SimpleResultStatus(str, Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"

    def __str__(self) -> str:
        return str(self.value)
