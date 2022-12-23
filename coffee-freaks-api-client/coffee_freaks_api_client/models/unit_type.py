from enum import Enum

class UnitType(str, Enum):
    KG = "kg"
    GRAM = "gram"
    PIECE = "piece"

    def __str__(self) -> str:
        return str(self.value)
