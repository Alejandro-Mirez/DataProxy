from enum import Enum

class BeansKind(str, Enum):
    ARABICA = "arabica"
    ROBUSTA = "robusta"
    LIBERICA = "liberica"

    def __str__(self) -> str:
        return str(self.value)
