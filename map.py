from tile import Tile, TileType
from colorama import Fore
from colorama import Style

class Map:
    def __init__(self, map = '', height = 0, width = 0) -> None:
        self.width = int(width)
        self.height = int(height)
        self.tiles = [[None for x in range(self.width)] for y in range(self.height)]
        self.generate(map)

    def generate(self, map):
        for y in range(self.height):
            for x in range(self.width):
                # Create a tile from the first 3 elements in the map string and then remove them from them
                self.tiles[y][x] = (Tile(map[:3]))
                map = map[3:]

    # print the map with different colors for different types of tiles
    def print(self):
        colour = Fore.GREEN
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[y][x].type == TileType.Snow:
                    colour = Fore.YELLOW
                elif self.tiles[y][x].type == TileType.Ice:
                    colour = Fore.BLUE
                elif self.tiles[y][x].type == TileType.Thick_Snow:
                    colour = Fore.RED
                elif self.tiles[y][x].type == TileType.Mountain:
                    colour = Fore.GREEN
                print(f"{colour}{self.tiles[y][x].name[0]}{Style.RESET_ALL}", end=' ')
            print()