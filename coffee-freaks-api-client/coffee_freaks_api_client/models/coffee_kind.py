from enum import Enum

class CoffeeKind(str, Enum):
    BEANS = "beans"
    CAPSULES = "capsules"
    GROUND = "ground"
    INSTANT = "instant"

    def __str__(self) -> str:
        return str(self.value)
