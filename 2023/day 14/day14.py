import os


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def transpose(data: list) -> list:
    transposed = list()
    for y in range(len(data[0])):
        transposed_row = ''
        for x in range(len(data)):
            transposed_row += data[x][y]
        transposed.append(transposed_row)
    return transposed


def rot90(data: tuple[str]) -> list[str]:
    rotated = []
    for y in range(len(data[0])-1, -1, -1):
        rotated_row = ""
        for x in range(len(data[0])):
            rotated_row += data[y][x]
        rotated.append(rotated_row)
    return rotated


def part_1(map: list) -> int:
    load = 0
    rows = len(map[0])
    for line in map:
        rocks = [i for i, r in enumerate(line) if r == 'O']
        roll_load = [rows - max(0, line[:r].rfind('#')) - line[max(0, line[:r].rfind('#')):r].count('O') - (1*line[:r].rfind('#') > -1) for r in rocks]
        load += sum(roll_load)
    return load


def part_2(map: list) -> int:
    rows = len(map[0])
    for line in map:
        rocks = [i for i, r in enumerate(line) if r == 'O']
        roll_load = [rows - max(0, line[:r].rfind('#')) - line[max(0, line[:r].rfind('#')):r].count('O') - (1*line[:r].rfind('#') > -1) for r in rocks]
        load += sum(roll_load)
    return load


if __name__ == '__main__':
    reflector = get_file()
    print(part_1(transpose(reflector)))
