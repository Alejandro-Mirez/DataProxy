from enum import Enum

class CoffeeKind(str, Enum):
    BEANS = "beans"
    GROUND = "ground"
    CAPSULES = "capsules"
    INSTANT = "instant"

    def __str__(self) -> str:
        return str(self.value)
