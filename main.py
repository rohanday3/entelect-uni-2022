from operator import add
from turtle import width
from tqdm import tqdm
from genericpath import exists
import sys,os
from map import Map
from resource import Resource, ResourceType
from tile import Tile, TileType
from resource import Resource, ResourceType, Item
from path import PathFinder
from calculate_score import Score
import json

def outJson(path, file):
    x = {
        "Party": ["Scout", "Gatherer"],
        "Path": path,
    }
    with open(file, 'w') as f:
        f.write(json.dumps(x))

def addResourceItems(lines, items, type):
    for line in lines:
        items.append(Item(list(map(int,line.split(','))),ResourceType[type]))
        # print(Item(list(map(int,line.split(','))),ResourceType[type]))

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python main.py <map_file>")
        sys.exit(1)

    if not exists(sys.argv[1]):
        print("Error: File does not exist")
        sys.exit(1)
    else:
        print("Opening file...")

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # extract information from txt file
    print("Extracting info...")
    step_allowance = int(lines[0][15:])
    n = 0
    resource_items = []
    for i in range(2,len(lines)):
        if lines[i] == "\n":
            continue
        if lines[i][0] in ["C","F","S"] and n<3:
            n += 1
            resource_type, quantity = lines[i].split(',')
            quantity = int(quantity)
            if resource_type == "Coal":
                coals = Resource(ResourceType.Coal, quantity)
            elif resource_type == "Fish":
                fish=Resource(ResourceType.Fish,quantity)
            elif resource_type == "Scrap_metal":
                scrap_metal = Resource(ResourceType.Scrap_metal,quantity)
            addResourceItems(lines[i+1:i+quantity+1],resource_items,resource_type)
            # print(lines[i+1:i+quantity],resource_items,resource_type)
        elif lines[i][0] == "Q" and lines[i+1][0] == "Q":
            quota = lines[i][6:].split(',')
            quota_multiplier = float(lines[i+1][17:])
        elif lines[i][0] == "m":
            height,width = list(map(int,lines[i][9:].split(',')))
            map = []
            for y in range(height):
                map.append(lines[i+y+1][:-1].split(','))
            
    print("Creating map...")
    print(f"Height: {height} Width: {width}")
    # print([[item.x, item.y, item.type] for item in resource_items])
    aMap = Map(map, height, width, resource_items)

    # astar = aStar()
    # path = astar.aStar(aMap, [0, 0], [width, height])
    # path = Solve(aMap, height,width, resource_items)
    aMap.print(resources=True)
    aPath = PathFinder(aMap,True)
    print(aPath.path)
    outJson(aPath.path, sys.argv[1][0]+"_out.txt")
    aMap.printPath(aPath.path)
    score = Score(resource_items,quota,quota_multiplier,step_allowance,aPath.path, aMap)

    print("Printing map...")
    # aMap.print()
    print("Score: ",score.calculate_score())
    print("Done")