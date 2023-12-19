import os
from queue import PriorityQueue


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    data = data.split('\n')
    return [tuple(r.split(' ')) for r in data]


def get_coords(plan: list) -> list:
    start = (0, 0)
    coords = [start, ]
    p = -1
    for step in plan:
        dir, dist, color = step
        dist = int(dist)
        p += dist
        if dir == 'U':
            start = (start[0] - dist, start[1])
        elif dir == 'R':
            start = (start[0], start[1] + dist)
        elif dir == 'D':
            start = (start[0] + dist, start[1])
        elif dir == 'L':
            start = (start[0], start[1] - dist)
        coords.append(start)
    return (coords, p)


def calc_area(coords: list) -> int:
    coords, p = coords
    total = 0
    # coords=[(4, 10), (9, 7), (11, 2), (2, 2), (4, 10)]
    print(coords)
    for i in range(len(coords) - 1):
        x1 = coords[i][0]
        y1 = coords[i][1]
        x2 = coords[i + 1][0]
        y2 = coords[i + 1][1]
        total += (x1 * y2) - (x2 * y1)
        print(f'({x1} * {y2}) - ({x2} * {y1}) = {x1 * y2} - {x2 * y1} = {(x1 * y2) - (x2 * y1)}. Total: {total}')
    return abs(total / 2) + (p//2 + 1)


def part_1(plan: list) -> int:
    coords = get_coords(plan)
    return calc_area(coords)

if __name__ == '__main__':
    plan = get_file()
    print(part_1(plan))
