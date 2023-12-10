import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def make_map(data: list) -> (tuple, dict):
    map = dict()
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == '.':
                continue
            if char == '|':
                x1 = x - 1
                y1 = y
                x2 = x + 1
                y2 = y  
            elif char == '-':
                x1 = x
                y1 = y - 1
                x2 = x
                y2 = y + 1
            elif char == 'L':
                x1 = x - 1
                y1 = y
                x2 = x
                y2 = y + 1
            elif char == 'J':
                x1 = x - 1
                y1 = y
                x2 = x
                y2 = y - 1
            elif char == '7':
                x1 = x
                y1 = y - 1
                x2 = x + 1
                y2 = y
            elif char == 'F':
                x1 = x + 1
                y1 = y
                x2 = x
                y2 = y + 1
            elif char == 'S':
                start = (x, y)
                x1 = x
                y1 = y - 1
                x2 = x + 1
                y2 = y
            map.update({(x, y): [(x1, y1), (x2, y2)]})
    return start, map


def part1(start: tuple, map: dict) -> int:
    route = dict()
    route.update({start: 0})
    for iter in range(2):
        prev = start
        steps = 0
        this = map[start][iter]
        while this != start:
            steps += 1
            if this not in route:
                route.update({this: steps})
            elif route[this] > steps:
                route[this] = steps
            if map[this][0] == prev:
                next = map[this][1]
            else:
                next = map[this][0]
            prev = this
            this = next
    return route[max(route, key=route.get)]


if __name__ == '__main__':
    input = get_file()
    start, map = make_map(input)
    print(part1(start, map))
