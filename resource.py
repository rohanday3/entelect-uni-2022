from enum import Enum
from turtle import distance
import math

class ResourceType(Enum):
    Coal = 200
    Fish = 400
    Scrap_metal = 1000

    def __str__(self) -> str:
        return self.name[0]

class Resource:
    def __init__(self, type, quantity) -> None:
        self.type = type
        self.quantity = quantity

    def getDistance(self, position, item):
        distance = math.sqrt((item.x - position[1])**2 + (item.y - position[0])**2)
        return distance

    def getClosest(self,position,items):
        position_x = position[0]
        position_y = position[1]
        distance = self.getDistance(position_x, position_y, items[0][1], items[0][0])
        for item in items:
            if self.getDistance(position_x, position_y, item[1], item[0]) < distance:
                closest = item
        return closest

    # function that returns an item from location
    def getItem(items,location):
        for item in items:
            if item.x == location[1] and item.y == location[0]:
                return item
        return None

class Item:
    def __init__(self, position, type) -> None:
        # Position is a tuple of (y,x)
        self.y,self.x = position
        self.type = type