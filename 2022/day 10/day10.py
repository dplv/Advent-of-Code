import os


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').readlines()
    return [line.replace('\n', '').split() for line in lines]


if __name__ == '__main__':
    INSTRUCTIONS = read_input()

    REGISTER = 1
    CYCLES = []
    SCREEN = []

    for instruction in INSTRUCTIONS:
        CYCLES.append(REGISTER)
        if instruction[0] == 'addx':
            CYCLES.append(REGISTER)
            REGISTER = REGISTER + int(instruction[1])

    print(sum([(REGISTER + 1) * CYCLES[REGISTER] for REGISTER in range(19, 220, 40)])) #part 1

    for cycle in range(240):
        sprite_position = (CYCLES[cycle] - 1, CYCLES[cycle], CYCLES[cycle] + 1)
        if cycle % 40 in sprite_position:
            SCREEN.append('#')
        else:
            SCREEN.append('.')

    for i, pixel in enumerate(SCREEN): # part 2
        print(pixel, end='')
        if i in range(39, 241, 40):
            print()

'''
####.#..#...##.####.###....##.####.####.
...#.#.#.....#.#....#..#....#.#.......#.
..#..##......#.###..###.....#.###....#..
.#...#.#.....#.#....#..#....#.#.....#...
#....#.#..#..#.#....#..#.#..#.#....#....
####.#..#..##..#....###...##..#....####.
ZKJFBJFZ
'''
