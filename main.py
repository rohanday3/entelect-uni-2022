from tqdm import tqdm
from genericpath import exists
import sys,os
from map import Map

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

    print("Creating object...")
    height, width = lines[0][9:].split(',')
    print("Height: " + height + " Width: " + width)
    aMap = Map(lines[2], height, width)
    print("Printing object...")
    aMap.print()
    print("Done")

    print("Test")