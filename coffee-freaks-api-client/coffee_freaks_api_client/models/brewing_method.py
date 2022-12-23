from enum import Enum

class BrewingMethod(str, Enum):
    ESPRESSO = "espresso"
    DRIP = "drip"

    def __str__(self) -> str:
        return str(self.value)
