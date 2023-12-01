import os
import re


def get_file():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    return file.readlines()


def part_1(data):
    sum = 0

    for line in data:
        line = re.findall(r'(\d)', line.replace('\n', ''))
        sum += int(line[0] + line[-1])

    return sum


def part_2(data):
    DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sum = 0

    for line in data:
        line = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line.replace('\n', ''))
        line = [str(DIGITS[s]) if s in DIGITS else s for s in line]
        sum += int(line[0] + line[-1])

    return sum


if __name__ == '__main__':
    input = get_file()
    
    p1 = part_1(input)
    print(p1)

    p2 = part_2(input)
    print(p2)
