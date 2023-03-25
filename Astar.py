import math
import heapq

import AStarAlogrithm
from Map import Map
from Node import Node


class AStarFinder:

    def __init__(self):
        self.open_set = []
        self.closed_set = set()

    def find_path(self, m: Map):
        if m.coin is None:
            return None
        start_node = Node(location=m.bot, g_score=0, f_score=AStarAlogrithm.AstarUtils.heuristic(m.bot, m.coin.loc))
        self.open_set.append(start_node)

        while self.open_set:
            current_node: Node = heapq.heappop(self.open_set)
            # print(str(current_node.location.x) + " " + str(current_node.location.y))

            if current_node.location == m.coin.loc:
                path = []
                while current_node is not None:
                    path.append(current_node.location)
                    current_node = current_node.parent
                return path[::-1]

            self.closed_set.add(current_node)

            for neighbor in AStarAlogrithm.AstarUtils.get_neighbors(current_node, m):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = current_node.g_score + 1

                if neighbor not in self.open_set:
                    heapq.heappush(self.open_set, neighbor)
                elif tentative_g_score >= neighbor.g_score:
                    continue

                neighbor.g_score = tentative_g_score
                neighbor.f_score = tentative_g_score + AStarAlogrithm.AstarUtils.heuristic(neighbor.location, m.coin.loc)

        return None
