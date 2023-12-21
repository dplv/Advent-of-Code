import os
import numpy as np

def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    data = data.split('\n')
    #add rocks around the actual map
    data.insert(0, '#' * len(data[0]))
    data.append('#' * len(data[0]))
    for i in range(len(data)):
        data[i] = '#' + data[i] + '#'
    return data


def make_map(data: list) -> tuple[tuple, dict]:
    ROCK = '#'
    MAP = dict()
    source = (0, 0)
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[0]) - 1):
            MAP[(x, y)] = []
            for dir in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if data[x + dir[0]][y + dir[1]] != ROCK:
                    MAP[(x, y)].append((x + dir[0], y + dir[1]))
            if data[x][y] == 'S':
                source = (x, y)
    return source, MAP


def explore(map: dict, start: set, max_steps):
    queue = []
    visited = []
    d = 0
    
    if max_steps == 0:
        return len(start)
    
    for s in start:
        queue.append((s, d))

    while queue:
        m, d = queue.pop(0)
        d += 1
        for n in map[m]:
            if n not in visited:
                visited.append(n)

    reach = explore(map, set(visited), max_steps - 1)

    return reach


if __name__ == '__main__':
    STEPS = 64
    data = get_file()
    source, map = make_map(data)
    print(explore(map, (source, ), STEPS)) #part 1

    """
        Using the fact that there aren't any obstacles in the same row/col of the starting point:
        - The area grows like a diamond
        - Output must be a nice rhombus due to the sparsity of the obstacles and the fact that there's an empty rhombus-shaped band in the input
        - After expanding by X, the corners of the diamond are the "start points", just shifted up/down/left/right.
        - 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
    """

    # polynomial extrapolation
    a0 = explore(map, (source, ), 65)
    a1 = explore(map, (source, ), 65 + 131)
    a2 = explore(map, (source, ), 65 + 2 * 131)

    vandermonde = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array([a0, a1, a2])
    x = np.linalg.solve(vandermonde, b).astype(np.int64)

    # note that 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
    n = 202300
    print("part 2:", x[0] * n * n + x[1] * n + x[2]) #74523846505198 too low