import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    data = data.split('\n')
    instructions = data[0]
    network = {
        node.split(' = ')[0]: 
        tuple(node.split(' = ')[1].replace('(', '').replace(')', '').split(', ')) for node in data[2:]
        }
    return instructions, network


def part1(data: tuple[str, dict]) -> int:
    instructions, network = data
    steps = 0
    node = 'AAA'
    finish = 'ZZZ'
    while node != finish:
        dir = instructions[steps % len(instructions)]
        dir = 0 if dir == 'L' else 1
        node = network[node][dir]
        steps += 1
    return steps


def part2(data: tuple[str, dict]) -> int:
    """
        For each start node **A, find number of steps to reach its finish node **Z
        Find Least Common Multiple between all steps
    """
    instructions, network = data
    start = [node for node in network if node.endswith('A')]
    steps = list()
    for node in start:
        step = 0
        finish = node
        while not finish.endswith('Z'):
            dir = instructions[step % len(instructions)]
            dir = 0 if dir == 'L' else 1
            finish = network[finish][dir]
            step += 1
        steps.append(step)
    return math.lcm(*steps)


if __name__ == '__main__':
    input = get_file()
    print(part1(input))
    print(part2(input))
