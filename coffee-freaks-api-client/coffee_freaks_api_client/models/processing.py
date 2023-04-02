from enum import Enum

class Processing(str, Enum):
    HONEY = "honey"
    NATURAL = "natural"
    WASHED = "washed"

    def __str__(self) -> str:
        return str(self.value)
