import os


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    patterns = data.split('\n\n')
    patterns = [pattern.split('\n') for pattern in patterns]
    return patterns


def transpose_pattern(pattern: list) -> list:
    transposed = list()
    for y in range(len(pattern[0])):
        transposed_row = list()
        for x in range(len(pattern)):
            transposed_row.append(pattern[x][y])
        transposed.append(''.join(transposed_row))
    return transposed


def get_reflection_row(pattern: list, part:int = 1) -> int:
    for r in range(1, len(pattern)):
        rows_in_reflection = min(r, len(pattern) - r)
        above = slice(r - rows_in_reflection, r)
        below = slice(r, r + rows_in_reflection)
        str_above = ''.join(pattern[above])
        str_below = ''.join(pattern[below][::-1])
        if part ==1 and pattern[above] == pattern[below][::-1]:
            return r
        if part == 2 and len([str_above[i] for i in range(len(str_above)) if str_above[i] != str_below[i]]) == 1:
            return r
    return -1


def solution(patterns: list, part: int) -> int:
    summary = 0
    for i, pattern in enumerate(patterns):
        r = get_reflection_row(transpose_pattern(pattern), part)
        if r > 0:
            summary += r
        else:
            r = get_reflection_row(pattern, part)
            summary += r * 100
    return summary


if __name__ == '__main__':
    patterns = get_file()
    print(solution(patterns, 1))
    print(solution(patterns, 2))
