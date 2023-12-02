import os
import re


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    return file.readlines()


def solution(data: list, bag: list = list) -> int:
    sum_1 = sum_2 = 0

    for line in data:
        id = int(re.findall(r'(?<=Game )+?(\d+)', line.replace('\n', ''))[0])
        red = max([int(n) for n in re.findall(r'\d+(?= red)', line.replace('\n', ''))])
        green = max([int(n) for n in re.findall(r'\d+(?= green)', line.replace('\n', ''))])
        blue = max([int(n) for n in re.findall(r'\d+(?= blue)', line.replace('\n', ''))])

        if red <= bag['red'] and green <= bag['green'] and blue <= bag['blue']:
            sum_1 += id

        sum_2 += red * green * blue

    return sum_1, sum_2


if __name__ == '__main__':
    input = get_file()
    bag = {'red': 12, 'green': 13, 'blue': 14}

    print(solution(input, bag))
