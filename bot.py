import argparse

from Astar import AStarFinder
from Map import Map

parser = argparse.ArgumentParser(description='Run bot.')
parser.add_argument('-i', '--input', type=str, help='Input file path')
parser.add_argument('-o', '--output', type=str, help='Output file path')
args = parser.parse_args()

if not args.input:
    print('Error: -i argument required.')
    exit()

if not args.output:
    print('Error: -o argument required.')
    exit()

try:
    with open(args.input, 'r') as f:
        my_map = Map(args.input, args.output)
        my_map.printMap()
        path = AStarFinder().find_path(my_map)
        print('My path: ', path)
        if path is not None:
            for i in path:
                if not my_map.moveTo(i):
                    continue
except FileNotFoundError:
    print(f'Error: File not found')
    exit()


