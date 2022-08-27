from tile import Tile, TileType
from colorama import Fore
from colorama import Style
from resource import Resource, ResourceType

class Map:
    def __init__(self, map, h, w, resources) -> None:
        self.width = w
        self.height = h
        self.tiles = [[None for x in range(self.width)] for y in range(self.height)]
        self.resources = resources
        self.generate(map)
        self.diff_map = self.createDiffMap()

    def generate(self, map):
        for y in range(self.height):
            for x in range(self.width):
                self.tiles[y][x] = Tile(TileType[map[y][x]], (y, x), Resource.getItem(self.resources, [y, x]))

    # print the map with different colors for different types of tiles
    def print(self, resources = False):
        colour = Fore.GREEN
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[y][x].type == TileType.S:
                    colour = Fore.CYAN
                elif self.tiles[y][x].type == TileType.I:
                    colour = Fore.WHITE
                elif self.tiles[y][x].type == TileType.TS:
                    colour = Fore.BLUE
                elif self.tiles[y][x].type == TileType.M:
                    colour = Fore.YELLOW
                if resources and self.tiles[y][x].item != None:
                    key = self.tiles[y][x].item.type
                    colour = Fore.RED
                else:
                    key = self.tiles[y][x].type
                print(f"{colour}{key}{Style.RESET_ALL}", end=' ')
            print()

    # print map showing path taken
    def printPath(self, path):
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) in path:
                    print(Fore.RED + "X" + Style.RESET_ALL, end=' ')
                else:
                    print(self.tiles[y][x].type, end=' ')
            print()


    # create array of difficulty for each tile
    def createDiffMap(self):
        diff_map = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                diff_map[y][x] = self.tiles[y][x].difficulty
        return diff_map