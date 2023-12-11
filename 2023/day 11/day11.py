import os


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def transpose_map(map: list) -> list:
    transposed_map = list()
    for x, row in enumerate(map):
        transposed_map.append(['.'] * len(row))
        for y, _ in enumerate(row):
            transposed_map[x][y] = map[y][x]
    return transposed_map


def expand_map(map: list) -> dict:
    transposed_map = transpose_map(map)
    empty_rows = [i for i in range(len(map)) if set(map[i]) == {'.'}]
    empty_cols = [i for i in range(len(transposed_map)) if set(transposed_map[i]) == {'.'}]
    return {'rows': empty_rows, 'cols': empty_cols}


def get_galaxies(map: list) -> tuple:
    galaxies = list()
    for x, row in enumerate(map):
        for y, _ in enumerate(row):
            if map[x][y] == '#':
                galaxies.append((x, y))
    return tuple(galaxies)


def solution(map: list, expansion_rate: int) -> int:
    galaxies = get_galaxies(map)
    expansion = expand_map(map)
    rows_expansion, cols_expansion = expansion.values()
    steps = 0
    for i, galaxy in enumerate(galaxies):
        for n in galaxies[i+1:]:
            step = abs(galaxy[0] - n[0]) + abs(galaxy[1] - n[1])
            rows = len([r for r in rows_expansion if r > min(galaxy[0], n[0]) and r <= max(galaxy[0], n[0])]) * (expansion_rate - 1)
            cols = len([c for c in cols_expansion if c > min(galaxy[1], n[1]) and c <= max(galaxy[1], n[1])]) * (expansion_rate - 1)
            steps += step + rows + cols
    return steps


if __name__ == '__main__':
    map = get_file()
    print(solution(map, 2))
    print(solution(map, 1000000))
