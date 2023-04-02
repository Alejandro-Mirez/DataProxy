from enum import Enum

class UnitType(str, Enum):
    GRAM = "gram"
    KG = "kg"
    PIECE = "piece"

    def __str__(self) -> str:
        return str(self.value)
