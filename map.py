class ParentClass:
    def __init__(self, map = '', height = 0, width = 0) -> None:
        self.width = int(width)
        self.height = int(height)
        self.tiles = [[None for x in range(self.width)] for y in range(self.height)]
        self.generate(map)

    def generate(self, map):
        # Generate object from map
        return None

    def print(self):
        # Print the object
        return None