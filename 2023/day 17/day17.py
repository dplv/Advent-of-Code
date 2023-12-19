import os
from queue import PriorityQueue


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')



def peek(pq: PriorityQueue, item: tuple[int, int]) -> int:
    for q in pq.queue:
        if q[1] == item:
            return q[0]
    return -1


def A_star(map: list, start: tuple[int, int] = (0, 0), finish: tuple[int, int] = (0, 0)):
    #node(0, 0, 0) -> (x, y, distance from start + heuristic distance to finish)
    Q = PriorityQueue()
    Q.put((0, start))
    visited = dict()
    visited[start] = ((0, 0), 0)

    while Q:
        q = Q.get()
        successors = get_successors(q[1], (len(map), len(map[0])), visited)
        for s in successors:
            if s == finish:
                return

            g = visited[q[1]][1] + int(map[s[0]][s[1]])
            h = abs(s[0] - finish[0]) + abs(s[1] - finish[1])
            f = peek(Q, s)
            if f > g + h: continue
            if s in visited and f > visited[s][1]: continue
            Q.put((g, s))

        x, y = visited[q[1]][0]
        visited[q[1]] = visited[q[1]][1] + int(map[x][y])


def get_successors(n: tuple[int, int], boundaries: tuple[int, int], visited: dict) -> tuple:
    successors = set()
    for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        x = n[0] + dir[0]
        y = n[1] + dir[1]
        if x >= 0 and y >= 0 and x < boundaries[0] and y < boundaries[1] and (x, y) not in visited:
            successors.add((n[0] + dir[0], n[1] + dir[1]))
    return successors
 

def part_2(map: list) -> int:
    edge_tiles = []
    edge_tiles += [(0, x, 'D') for x in range(len(map[0]))]             #top row
    edge_tiles += [(len(map) - 1, x, 'U') for x in range(len(map[0]))]  #bottom row
    edge_tiles += [(x, 0, 'R') for x in range(len(map))]                #left column
    edge_tiles += [(x, len(map[0]) - 1, 'L') for x in range(len(map))]  #right column

    return max([energize(map, start=tile) for tile in edge_tiles])


if __name__ == '__main__':
    data = get_file()

    print(A_star(data, (0, 0), (5, 5)))

    # pq = PriorityQueue()
    # pq.put((1, (0, 0)))
    # pq.put((4, (1, 2)))
    # pq.put((2, (0, 1)))
    # pq.put((3, (1, 0)))
    # pq.put((7, (1, 1)))

    # print(pq.queue[0])
    # print(pq.queue)
    # print(pq.get())
    # print(pq.queue)
    # print(pq.get())
    # print(pq.queue)
    # print(peek(pq, (1, 1)))
    # print(pq.queue)