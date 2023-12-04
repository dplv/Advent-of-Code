import os
import re


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def solution(data: list) -> (int, int):
    sum_p1 = 0
    pattern = r'[:](.*)[|](.*)'

    COPIES = [0] * len(data)

    for id, line in enumerate(data):
        numbers = re.findall(pattern, line)

        card = [int(x) for x in numbers[0][0].split(' ') if x.isdigit()]
        wins = [int(x) for x in numbers[0][1].split(' ') if x.isdigit()]
        points = len([1 for x in card if x in wins])
        sum_p1 += 2 ** (points - 1) if points > 0 else 0

        COPIES[id] += 1
        for c in range(id + 1, id + points + 1):
            COPIES[c] += COPIES[id]

    return sum_p1, sum(COPIES)


if __name__ == '__main__':
    input = get_file()

    print(solution(input))
