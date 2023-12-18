import os
from collections import defaultdict


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split(',')


def HASH(s: str) -> int:
    value = 0
    for c in s:
        v = ord(c)
        value += v
        value *= 17
        value = value % 256
    return value


def part_1(sequence: list) -> int:
    return sum([HASH(s) for s in sequence])


def get_label(lens: str) -> tuple:
    if lens.find('=') > 0:
        return (lens.split('=') + ['='])
    else:
        return (lens[:-1], None, '-')


def get_power(boxes: defaultdict) -> int:
    value = 0
    for box, lenses in boxes.items():
        value += sum([(box + 1) * (i + 1) * lenses[lens] for i, lens in enumerate(lenses)])
    return value


def part_2(sequence: list) -> int:
    boxes = defaultdict(defaultdict)
    for s in sequence:
        label, f, operation = get_label(s)
        box = HASH(label)

        if operation == '=':
            boxes[box][label] = int(f)
        elif label in boxes[box]:
            boxes[box].pop(label)

    return get_power(boxes)


if __name__ == '__main__':
    sequence = get_file()
    print(part_1(sequence))
    print(part_2(sequence))
