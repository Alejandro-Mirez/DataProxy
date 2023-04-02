from enum import Enum

class BrewingMethod(str, Enum):
    DRIP = "drip"
    ESPRESSO = "espresso"

    def __str__(self) -> str:
        return str(self.value)
