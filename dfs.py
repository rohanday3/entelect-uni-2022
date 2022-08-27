# class that implements the depth first search algorithm to find the shortest path between two tiles with the highest score

class Solve:
    def __init__(self, map, h, w, resources):
        self.width = w
        self.height = h
        self.resources = resources

    # Function to find a path between two tiles
    def stupidShortestPath(self):
        path = []
        position = [0, 0]
        while position != [self.width-1,self.height-1]:
            if position[0] != self.width-1:
                position[0] += 1
            elif position[1] != self.height-1:
                position[1] += 1
            path.append(position[::])
        print(path)
