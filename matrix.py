from AStarAlogrithm import Astar
from AStarAlogrithm import Location



#cho mot ma tran 7X11


matrix = [['*', '*', '*', '*', '*', '*', '*'],
          ['*', 'x', '*', ' ', ' ', 'o', '*'],
          ['*', ' ', '*', ' ', ' ', ' ', '*'],
          ['*', ' ', '*', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', ' ', ' ', ' ', ' ', ' ', '*'],
          ['*', '*', '*', '*', '*', '*', '*']]

path = Astar().find_path(Location(1, 1), Location(1, 5), 6, 11, matrix)
print('My path: ', path)



