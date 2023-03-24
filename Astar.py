import math
import heapq

class Node:
    def __init__(self, location, parent=None, g_score= float("inf"), f_score=float("inf")):
        self.location = location 
        self.parent = parent
        self.g_score = g_score
        self.f_score = f_score

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __lt__(self, other):
        return self.f_score < other.f_score

class Location:
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_score = 1
        self.f_score = 1
        self.parent = None

    def __repr__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False
    def __hash__(self):
        return hash((self.x, self.y))
    @staticmethod
    def sort(locations):
        return sorted(locations, key=lambda loc: (loc.x, loc.y))

    @staticmethod
    def heuristic(a, b) -> float:
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

class AStarFinder:

    def __init__(self):
        self.open_set = []
        self.closed_set = set()

    @staticmethod
    def heuristic(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)
    @staticmethod
    def get_neighbors(node: Node, width, height, matrix):
        neighbors = []
        for x_offset, y_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbor_location = Location(node.location.x + x_offset, node.location.y + y_offset)
            if matrix [neighbor_location.x][neighbor_location.y] == "*" or neighbor_location.x < 0 or neighbor_location.x >= height \
                    or neighbor_location.y < 0 or neighbor_location.y >= width:
                continue
            neighbor_node = Node(location=neighbor_location, parent=node)
            neighbors.append(neighbor_node)
        return neighbors
    def find_path(self,bot_loc, coin_loc, width, height, matrix):
        start_node = Node(location=bot_loc, g_score=0, f_score=self.heuristic(bot_loc, coin_loc))
        self.open_set.append(start_node)

        while self.open_set:
            current_node: Node = heapq.heappop(self.open_set)
            print(str(current_node.location.x) + " " +str(current_node.location.y))

            if current_node.location ==coin_loc:
                path = []
                while current_node is not None:
                    path.append(current_node.location)
                    current_node = current_node.parent
                return path[::-1]

            self.closed_set.add(current_node)

            for neighbor in self.get_neighbors(current_node,width, height, matrix ):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = current_node.g_score + 1

                if neighbor not in self.open_set:
                    heapq.heappush(self.open_set, neighbor)
                elif tentative_g_score >= neighbor.g_score:
                    continue

                neighbor.g_score = tentative_g_score
                neighbor.f_score = tentative_g_score + self.heuristic(neighbor.location, coin_loc)

        return None







        

