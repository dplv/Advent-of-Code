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


def rot90(data: list[str]) -> list[str]:
    rotated = []
    for y in range(len(data[0])-1, -1, -1):
        rotated_row = ''
        for x in range(len(data[0])):
            rotated_row += data[y][x]
        rotated.append(rotated_row)
    return rotated


def roll_map(map: list) -> list:
    rolled = []
    for row in map:
        new_row = ''
        dot_count = 0
        for rock in row:
            if rock == ".":
                dot_count += 1
            elif rock == "O":
                new_row += "O"
            else:
                new_row += "." * dot_count + "#"
                dot_count = 0
        new_row += '.' * dot_count
        rolled.append(new_row)
    return rolled


def cycle(map: list) -> tuple:
    for _ in range(4):
        map = roll_map(map)
        map = rot90(map)
    return tuple(map)

def part_1(map: list) -> int:
    load = 0
    rows = len(map[0])
    for line in map:
        rocks = [i for i, r in enumerate(line) if r == 'O']
        roll_load = [rows - max(0, line[:r].rfind('#')) - line[max(0, line[:r].rfind('#')):r].count('O') - (1*line[:r].rfind('#') > -1) for r in rocks]
        load += sum(roll_load)
    return load


def part_2(map: list) -> int:
    loops = {}
    for i in range(1000000000):
        new_map = cycle(map)
        if new_map not in loops:
            loops[new_map] = i
        elif (1000000000 - i) % (loops[new_map] - i) == 0:
            break
        map = new_map
    
    load = part_1(map)

    return load


if __name__ == '__main__':
    reflector = get_file()
    print(part_1(transpose(reflector)))
    print(part_2(transpose(reflector)))
