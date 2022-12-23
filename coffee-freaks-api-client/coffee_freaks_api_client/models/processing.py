from enum import Enum

class Processing(str, Enum):
    NATURAL = "natural"
    WASHED = "washed"
    HONEY = "honey"

    def __str__(self) -> str:
        return str(self.value)
