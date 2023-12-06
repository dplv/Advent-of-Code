import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def solution(data: list) -> (int, int):
    races = [(int(r[0]), int(r[1])) for r in zip(data[0].split()[1:], data[1].split()[1:])]
    #for part 2
    races.append((int(''.join(data[0].replace('Time:', '').split())), int(''.join(data[1].replace('Distance:', '').split()))))
    results = []

    for time, distance in races:
        d = (time ** 2) - (4 * 1 * distance)
        min_time = (time-math.sqrt(d))/2
        max_time = (time+math.sqrt(d))/2
        min_time = min_time + 0.1 if min_time.is_integer() else min_time
        max_time = max_time - 0.1 if max_time.is_integer() else max_time
        min_time = math.ceil(min_time)
        max_time = math.ceil(max_time)
        results.append(max_time - min_time)

        result_1 = 1
        for x in results[:-1]:
            result_1 = result_1 * x
        
    return result_1, results[-1]


if __name__ == '__main__':
    input = get_file()

    print(input)
    print(solution(input))
