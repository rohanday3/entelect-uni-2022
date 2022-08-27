from enum import Enum

class ResourceType(Enum):
    COAL = "C"
    FISH = "F"
    SCRAP_METAL = "M"

class Resource:
    def __init__(self, type, quantity, locations=[]) -> None:
        self.type = type
        self.items = self.generateItems(locations)
        self.quantity = quantity
        self.closest = self.getClosest(self.items)

    def generateItems(self,locations):
        for location in locations:
            self.items.append(Item(location[0], location[1]))
        return self.items

    def getClosest(self,items):
        closest = items[0]
        for item in items:
            if item.distance < closest.distance:
                closest = item
        return closest

class Item:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y