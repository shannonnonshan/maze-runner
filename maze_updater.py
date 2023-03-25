import argparse

from map import Map
from txtSequenceRead import TXT
from Astar import AStarFinder


parser = argparse.ArgumentParser(description='Regen coin.')
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
        TXT = TXT(args.input)
        path = TXT.getSeq()
        my_map = Map(args.output, args.input, False)
        if path is not None:
            if len(path) > 0:
                for step in path:
                    if step == "up":
                        if my_map.up():
                            my_map.moveUpdate()
                    elif step == "down":
                        if my_map.down():
                            my_map.moveUpdate()
                    elif step == "left":
                        if my_map.left():
                            my_map.moveUpdate()
                    elif step == "right":
                        if my_map.right():
                            my_map.moveUpdate()
                    my_map.printMap()
        elif path is None:
            my_map.moveUpdate()
            my_map.printMap()

except FileNotFoundError:
    print(f'Error: File not found')
    exit()


