import math
from queue import PriorityQueue

class aStar():

    def __init__(self, f, g, h):
        """
            F is the total cost of the node.
            G is the distance between the current node and the start node.
            H is the heuristic — estimated distance from the current node to the end node.
        """

        def get_g(curr_tile, next_tile):
            self.g = math.dist(curr_tile.location, next_tile.location)

        def get_h(curr_tile, next_tile):
            # score calculation here
            pass

        def get_f():
            self.f = self.g + self.h
            
        def is_in_queue(x, q):
            with q.mutex:
                return x in q.queue

        def get_neighbours(current, map):
            x, y = current.positon

            up = Node()
            down = Node()
            left = Node()
            right = Node()

            if y+1 < map.height:
                up = Node(current, [x, y+1])

            if y-1 > 0:
                down = Node(current, [x, y-1])
            
            if x-1 > 0:
                left = Node(current, [x-1, y])
            
            if x+1 < map.width:
                right = Node(current, [x+1, y])

            neighbours = [up, down, left, right]
            n = []
            for i in range(len(neighbours)-1, 0, -1):
                if neighbours[i].position != None:
                    n.append(neighbours[i])

            return n


        def aStar(map, start, end):
            # initialise open anc closed lists
            open_list = PriorityQueue()
            closed_list = PriorityQueue()

            start_node = Node(None, start)
            start_node.g = start_node.h = start_node.f = 0
            end_node = Node(None, end)
            end_node.g = end_node.h = end_node.f = 0

            # while openlist not empty
            while not open_list.empty():
                # Get the current node
                current_node = open_list.get()
                current_index = 0

                # Pop current off open list (happens already with get() above), add to closed list
                closed_list.put(current_node)

                # found goal
                if current_node == end_node:
                    path = []
                    current = current_node
                    while current is not None:
                        path.append(current.position)
                        current = current.parent
                    return path[::-1] # Return reversed path

                # find neighbours
                neighbours = get_neighbours(current)

                for neighbour in neighbours:
                    if is_in_queue(neighbour, open_list):
                        continue

                    neighbour.g = get_g(start, neighbour)
                    neighbour.h = get_h(start, neighbour)
                    neighbour.f = get_f()

                    open_list.put(neighbour)

    
class Node():

    def __init__(self, parent=None, pos=None):
        """
            F is the total cost of the node.
            G is the distance between the current node and the start node.
            H is the heuristic — estimated distance from the current node to the end node.
        """
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent
        self.position = pos