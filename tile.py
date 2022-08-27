from enum import Enum

class TileType(Enum):
    S = 1
    I = 5
    TS = 10
    M = 15

class Tile:
    def __init__(self,type:TileType,location, item = None) -> None:
        self.type = type
        self.difficulty = self.type.value
        self.location = location
        self.item = item

    # function that returns an tile from location
    def getTile(tiles,location):
        for tile in tiles:
            if tile.location[0] == location[0] and tile.location[1] == location[1]:
                return tile
        return None

    def __str__(self):
        return f"Type: {self.type}, Difficulty: {self.difficulty}, Location: {self.location}"

if __name__ == "__main__":
    t_test = [Tile(TileType.SNOW,(1,1)),Tile(TileType.ICE,(2,3)),Tile(TileType.THICK_SNOW,(3,4)),Tile(TileType.MOUNTAIN,(4,5))]
    print(Tile.getTile(t_test,[2,3]))
    