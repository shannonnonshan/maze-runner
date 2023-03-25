from map import Map
from Node import Node
from location import Location


# khoi tao vi tri

class AstarUtils:

    def __init__(self):
        self.open_set = []
        self.closed_set = set()

    @staticmethod
    def heuristic(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    @staticmethod
    def get_neighbors(node: Node, m: Map):
        neighbors = []
        for x_offset, y_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbor_location = Location(node.location.x + x_offset, node.location.y + y_offset)

            if neighbor_location in m.obstacles \
                    or neighbor_location.x < 0 or neighbor_location.x >= m.height \
                    or neighbor_location.y < 0 or neighbor_location.y >= m.width:
                continue
            neighbor_node = Node(location=neighbor_location, parent=node)
            neighbors.append(neighbor_node)
        return neighbors

