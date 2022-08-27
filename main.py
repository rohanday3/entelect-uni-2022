from operator import add
from turtle import width
from tqdm import tqdm
from genericpath import exists
import sys,os
from map import Map
from resource import Resource, ResourceType

def addResourceItems(lines, items, type):
    for line in lines:
        items.append(map(int,line.split()),type)

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
    step_allowance = lines[0][15:]
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
                coals = Resource(ResourceType.COAL, quantity)
            elif resource_type == "Fish":
                fish=Resource(ResourceType.FISH,quantity)
            elif resource_type == "Scrap Metal":
                scrap_metal = Resource(ResourceType.SCRAP_METAL,quantity)
            addResourceItems(lines[i+1:i+quantity], resource_items,resource_type)
        elif lines[i][0] == "Q" and lines[i+1][0] == "Q":
            quota = lines[i][6:].split(',')
            quota_multiplier = float(lines[i+1][17:])
        elif lines[i][0] == "m":
            height,width = list(map(int,lines[i][9:].split(',')))
            map = []
            for y in range(height):
                print([lines[i+y+1][:-1].split(',')])
                map.append([lines[i+y+1][:-1].split(',')])
            
    print("Creating map...")
    print(f"Height: {height} Width: {width}")
    # aMap = Map(map, height, width)
    print("Printing map...")
    # aMap.print()
    print("Done")