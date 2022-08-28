import heapq
import os
from queue import PriorityQueue
from tabnanny import verbose
from warnings import warn
from resource import Resource, ResourceType


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


class PathFinder:
    def __init__(self, map, score, verbose=False, heuristic_multiplier=0.8) -> None:
        self.map = map
        self.score = score
        self.verbose = verbose
        self.heuristic_multiplier = heuristic_multiplier
        self.solved = True
        self.start = (0, 0)
        self.width = self.map.width
        self.height = self.map.height
        self.end = (self.height - 1, self.width - 1)
        self.path = self.astar()

    def astar(self, allow_diagonal_movement=False):
        """
        Returns a list of tuples as a path from the given start to the given end in the given maze
        """

        # Create start and end node
        start_node = Node(None, self.start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, self.end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Heapify the open_list and Add the start node
        heapq.heapify(open_list)
        heapq.heappush(open_list, start_node)

        # Adding a stop condition
        outer_iterations = 0
        max_iterations = self.width * self.height  # // 2

        # what squares do we search
        adjacent_squares = (
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        )
        if allow_diagonal_movement:
            adjacent_squares = (
                (0, -1),
                (0, 1),
                (-1, 0),
                (1, 0),
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            )

        # Loop until you find the end
        while len(open_list) > 0:
            outer_iterations += 1

            if outer_iterations > max_iterations:
                # if we hit this point return the path such as it is
                # it will not contain the destination
                warn("giving up on pathfinding too many iterations")
                self.solved = False
                return return_path(current_node)

            # Get the current node
            current_node = heapq.heappop(open_list)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                return return_path(current_node)

            # Generate children
            children = []

            for new_position in adjacent_squares:  # Adjacent squares

                # Get node position
                node_position = (
                    current_node.position[0] + new_position[0],
                    current_node.position[1] + new_position[1],
                )

                # Make sure within range
                if (
                    node_position[0] > (self.height - 1)
                    or node_position[0] < 0
                    or node_position[1] > self.width - 1
                    or node_position[1] < 0
                ):
                    continue

                # TODO: Make sure walkable terrain
                # if self.map.tiles[node_position[0]][node_position[1]] != 0:
                #     continue

                # Create new node
                new_node = Node(
                    current_node,
                    node_position,
                    current_node.n + 1,
                    self.map.tiles[node_position[0]][node_position[1]].item,
                )

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:
                # Child is on the closed list
                if (
                    len(
                        [
                            closed_child
                            for closed_child in closed_list
                            if closed_child == child
                        ]
                    )
                    > 0
                ):
                    continue

                # Create the f, g, and h values
                child.g = current_node.g - (
                    self.score.calculate_next_step_score(
                        (child.position[0], child.position[1]),
                        child.n,
                        child.resources,
                    )
                    * self.heuristic_multiplier
                )
                # print("Node position: ", child.position)
                # print("n partents: ", child.n)
                # Euclidian distance not applicable for this problem
                # child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                #     (child.position[1] - end_node.position[1]) ** 2
                # )
                # calculate manhattan distance
                child.h = abs(child.position[0] - end_node.position[0]) + abs(
                    child.position[1] - end_node.position[1]
                )
                child.f = child.g + child.h

                # print(child.position, child.h, "g: ", child.g, "f: ", child.f)
                # print()

                # Child is already in the open list
                if (
                    len(
                        [
                            open_node
                            for open_node in open_list
                            if child.position == open_node.position
                            and child.g > open_node.g
                        ]
                    )
                    > 0
                ):
                    continue

                # Add the child to the open list
                heapq.heappush(open_list, child)
        warn("Couldn't get a path to destination")
        return None


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None, n=0, resource=None):
        self.parent = parent
        # position is a tuple of (y,x)
        self.position = position
        self.n = n
        self.g = 0
        self.h = 0
        self.f = 0
        self.resources = self.path_resources(resource)

    def path_resources(self, resource):
        if resource != None:
            return self.parent.resources + [resource]
        if self.n > 0:
            return self.parent.resources
        return []

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f
