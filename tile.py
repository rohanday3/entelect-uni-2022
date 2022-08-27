from enum import Enum

class TileType(Enum):
    Snow = "S"
    Ice = "I"
    Thick_Snow = "T"
    Mountain = "M"

class Tile:
    def __init__(self,elevation=0) -> None:
        self.elevation = int(elevation)
        self.name = self.calculateType()
        self.type = TileType[self.name]

    # 0-100 Snow
    # 101-150 Ice
    # 151-175 Thick Snow
    # 176-255 Mountain
    def calculateType(self):
        if self.elevation < 101:
            return "Snow"
        elif self.elevation < 151:
            return "Ice"
        elif self.elevation < 176:
            return "Thick_Snow"
        else:
            return "Mountain"

    