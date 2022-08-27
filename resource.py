from enum import Enum

class ResourceType(Enum):
    COAL = "C"
    FISH = "F"
    SCRAP_METAL = "M"

class Resource:
    def __init__(self, type, quantity, locations=[]) -> None:
        self.type = type
        self.locations = locations
        self.quantity = quantity