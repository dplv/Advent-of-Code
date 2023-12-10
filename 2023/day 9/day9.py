import os


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    data = data.split('\n')
    data = [[int(x) for x in line.split(' ')] for line in data]
    return data


def part1(data: list) -> int:
    value = 0
    for history in data:
        
        levels = [history, ]
        while not all([i == 0 for i in history]):
            diff = [history[i] - history[i-1] for i in range(1, len(history))]
            levels.append(diff)
            history = diff
        
        levels = levels[::-1]
        for i, _ in enumerate(levels[1:]):
            levels[i + 1].append(levels[i+1][-1] + levels[i][-1])
        value += levels[-1][-1]
    
    return value


def part2(data: list) -> int:
    value = 0
    for history in data:
        history = [0] + history

        levels = [history, ]
        while not all([i == 0 for i in history[1:]]):
            diff = [history[i] - history[i-1] for i in range(1, len(history))]
            levels.append(diff)
            history = diff

        levels[-1][0] = 0
        levels = levels[::-1]
        for i, _ in enumerate(levels[1:]):
            levels[i + 1][0] = levels[i + 1][1] - levels[i][0]
        value += levels[-1][0]
    
    return value


if __name__ == '__main__':
    input = get_file()
    print(part1(input))
    print(part2(input))
