from enum import Enum
from turtle import distance
import math

class ResourceType(Enum):
    COAL = 200
    FISH = 400
    SCRAP_METAL = 1000

class Resource:
    def __init__(self, type, quantity) -> None:
        self.type = type
        self.quantity = quantity
        self.closest = self.getClosest(self.items)

    def getDistance(self, position, item):
        distance = math.sqrt((item.x - position[0])**2 + (item.y - position[1])**2)
        return distance

    def getClosest(self,position,items):
        position_x = position[0]
        position_y = position[1]
        distance = self.getDistance(position_x, position_y, items[0][0], items[0][1])
        for item in items:
            if self.getDistance(position_x, position_y, item[0], item[1]) < distance:
                closest = item
        return closest

    # function that returns an item from location
    def getItem(self,items,location):
        for item in items:
            if item.x == location[0] and item.y == location[1]:
                return item
        return None

class Item:
    def __init__(self, position, type) -> None:
        self.x = position[0]
        self.y = position[1]
        self.type = type