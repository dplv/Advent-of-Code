import os


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').readlines()
    lines = [list(line.replace('\n', '')) for line in lines]
    return lines


def make_heightmap() -> dict:
    DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

    data = read_input()
    map = dict()

    for i in range(len(data)):
        for j in range(len(data[0])):
            map[(i, j)] = list()
            height = data[i][j]

            if height == 'S':
                source = (i, j)
                height = 'a'
            elif height == 'E':
                dest = (i, j)
                height = 'z'

            for dir in DIRS:
                if i + dir[0] < 0 or j + dir[1] < 0:
                    continue
                try:
                    elevation = data[i + dir[0]][j + dir[1]]
                    elevation = 'z' if elevation == 'E' else elevation
                    elevation = 'a' if elevation == 'S' else elevation
                    if ord(elevation) <= ord(height) + 1:
                        map[(i, j)].append((i + dir[0], j + dir[1]))
                except IndexError:
                    continue
                
    return {
        'source': source,
        'dest': dest,
        'map': map
    }


def BFS_path(map: dict, source: set, destination: set) -> int:
    Q = list()
    visited = set()
    dist = {v: 0 for v in map}

    Q.append(source)
    visited.add(source)

    while Q:
        v = Q.pop(0)
        if v == destination:
            return dist[v]
        for w in map[v]:
            if w not in visited:
                visited.add(w)
                dist[w] = dist[v] + 1
                Q.append(w)


def descent(data: list, map: dict, destination: set) -> int:
    best_steps = float('inf')

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in ('a', 'S'):
                steps = BFS_path(map, (i, j), destination)
                if steps and steps < best_steps:
                    best_steps = steps
    
    return best_steps


if __name__ == '__main__':
    data = read_input()
    source, dest, map = [*make_heightmap().values()]
    
    steps_up = BFS_path(map, source, dest)
    print(steps_up) #part 1
    
    steps_down = descent(data, map, dest)
    print(steps_down) #part 2
