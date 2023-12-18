import os
from collections import deque


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def move(node, map):
    x, y, d = node
    c = map[x][y] + d

    #Turns
    if c in ['/R', '\\L']:      d = 'U'
    elif c in ['/U', '\\D']:    d = 'R'
    elif c in ['/L', '\\R']:    d = 'D'
    elif c in ['/D', '\\U']:    d = 'L'

    #Splits
    elif c in ['|R', '|L']:
        return move((x, y, 'U'), map) + move((x, y, 'D'), map)
    elif c in ['-U', '-D']:
        return move((x, y, 'L'), map) + move((x, y, 'R'), map)

    #Forward moves
    if d == 'U':    x -= 1
    elif d == 'R':  y += 1
    elif d == 'D':  x += 1
    elif d == 'L':  y -= 1

    #Out of bounds
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return []

    return [(x, y, d)]


def energize(map: list, start: tuple[int, int, str] = (0, 0, 'R')) -> int:
    #start = (x, y, direction)
    Q = deque([start])
    visited = set()

    while Q:
        node = Q.popleft()
        if node in visited: continue

        visited.add(node)
        next = move(node, map)
        Q.extend(next)

    visited = set([(n[0], n[1]) for n in visited])

    return len(visited)


def part_2(map: list) -> int:
    edge_tiles = []
    edge_tiles += [(0, x, 'D') for x in range(len(map[0]))]             #top row
    edge_tiles += [(len(map) - 1, x, 'U') for x in range(len(map[0]))]  #bottom row
    edge_tiles += [(x, 0, 'R') for x in range(len(map))]                #left column
    edge_tiles += [(x, len(map[0]) - 1, 'L') for x in range(len(map))]  #right column

    return max([energize(map, start=tile) for tile in edge_tiles])


if __name__ == '__main__':
    data = get_file()
    p1 = energize(data)
    print(p1)
    
    p2 = part_2(data)
    print(p2)
