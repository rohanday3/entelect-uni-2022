from enum import Enum
from turtle import distance
import math

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

    def getDistance(self, x, y, a, b):
        distance = math.sqrt((x - a)**2 + (y - b)**2)
        return distance

    def getClosest(self,items, position):
        position_x = position[0]
        position_y = position[1]
        distance = self.getDistance(position_x, position_y, items[0][0], items[0][1])
        for item in items:
            if self.getDistance(position_x, position_y, item[0], item[1]) < distance:
                closest = item
        return closest

class Item:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y