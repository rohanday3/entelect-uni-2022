from enum import Enum

class TileType(Enum):
    S = 1
    I = 5
    TS = 10
    M = 15
    def __str__(self) -> str:
        return self.name[0]

class Tile:
    def __init__(self,type:TileType,location, item = None) -> None:
        self.type = type
        self.difficulty = self.type.value
        # Location is a tuple of (y,x)
        self.location = location
        self.item = item

    # function that returns an tile from location
    def getTile(tiles,location):
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x].location[0] == location[0] and tiles[y][x].location[1] == location[1]:
                    return tiles[y][x]
        return None

    # def __str__(self):
    #     return f"Type: {self.type}, Difficulty: {self.difficulty}, Location: {self.location}"

if __name__ == "__main__":
    t_test = [Tile(TileType.S,(1,1)),Tile(TileType.I,(2,3)),Tile(TileType.TS,(3,4)),Tile(TileType.M,(4,5))]
    print(Tile.getTile(t_test,[2,3]))
    