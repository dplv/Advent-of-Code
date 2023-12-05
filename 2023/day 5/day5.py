import os
import re


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n\n')


def solution(data: list) -> (int, int):
    seeds = [int(x) for x in re.findall(r'\d+', data[0])]
    seeds_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    maps = [m.split('\n')[1:] for m in data[1:]]

    for m in maps:
        temp_seed = seeds.copy()
        for map_line in m:
            map_line = [int(x) for x in map_line.split()]
            for s, seed in enumerate(temp_seed):
                if seed in range(map_line[1], map_line[1] + map_line[2]):
                    seeds[s] = seed + (map_line[0] - map_line[1])

    return min(seeds)


if __name__ == '__main__':
    input = get_file()

    print(solution(input))
