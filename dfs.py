# class that implements the depth first search algorithm to find the shortest path between two tiles with the highest score

class Solve:
    def __init__(self, map, h, w, resources):
        self.width = w
        self.height = h
        self.tiles = [[None for x in range(self.width)] for y in range(self.height)]
        self.resources = resources
        self.generate(map)

    # Function to find a path between two tiles with the highest score
    def getPath(self):
        # Initialise open and closed lists
        open_list = PriorityQueue()
        closed_list = PriorityQueue()

        # Create start and end nodes
        start_node = Node(None, [0, 0])
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, [self.width-1, self.height-1])
        end_node.g = end_node.h = end_node.f = 0

        # While open list is not empty
        while open_list.empty():
            # Get the current node
            current_node = open_list.get()
            # Pop current off open list (happens already with get() above), add to closed list
            closed_list.put(current_node)
            # found goal
            if current_node == end_node:
                path = []
                current = current_node
                # while current is not None:
                #     path.append(current.position)
                #     current = current.parent
                return path[::-1]
