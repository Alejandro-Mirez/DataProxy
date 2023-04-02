from enum import Enum

class BeansKind(str, Enum):
    ARABICA = "arabica"
    LIBERICA = "liberica"
    ROBUSTA = "robusta"

    def __str__(self) -> str:
        return str(self.value)
