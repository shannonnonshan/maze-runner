import math


class Location:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def sort(locations):
        return sorted(locations, key=lambda loc: (loc.x, loc.y))
