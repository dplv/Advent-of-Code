import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    data = data.split('\n')
    data = [[int(x) for x in line.split(' ')] for line in data]
    return data


def part1(data: list) -> int:
    for history in data:
        diff = [history[i] - history[i-1] for i in range(1, len(history))]
        print(diff)


if __name__ == '__main__':
    input = get_file()
    print(part1(input))
