import os
import math


class Monkey():
    def __init__(self, id) -> None:
        self.id = id
        self.items = list()
        self.inspected = 0
        self.operation = str
        self.test = str
        self.test_true = str
        self.test_false = str


def read_input():
    MONKEYS = list()
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').readlines()
    for i in range(len(lines)):
        if lines[i].startswith('Monkey'):
            id = int(lines[i].split(' ')[1].replace(':', ''))
            monkey = Monkey(id)
            monkey.items = list(map(int, lines[i + 1].replace('\n', '').replace('Starting items: ', '').replace(' ', '').split(',')))
            monkey.operation = lines[i + 2].replace('\n', '').replace('Operation: new = old ', '').replace('* old', '** 2')
            monkey.test = int(lines[i + 3].replace('\n', '').split()[-1])
            monkey.test_true = int(lines[i + 4].replace('\n', '').rsplit()[-1])
            monkey.test_false = int(lines[i + 5].replace('\n', '').rsplit()[-1])
            MONKEYS.append(monkey)
        try:
            _ = lines[i + 7]
        except IndexError:
            pass
    return MONKEYS


if __name__ == '__main__':
    MONKEYS = read_input()
    ROUNDS = 10000

    mod_factor = math.prod([monkey.test for monkey in MONKEYS])

    for round in range(ROUNDS):
        for monkey in MONKEYS:
            for item in monkey.items:
                monkey.inspected += 1
                worry_level = eval(f'{item} {monkey.operation}')
                worry_level %= mod_factor
                # worry_level = worry_level // 3 #part 1
                if worry_level % monkey.test == 0:
                    MONKEYS[monkey.test_true].items.append(worry_level)
                else:
                    MONKEYS[monkey.test_false].items.append(worry_level)
            monkey.items.clear()

    most_active = sorted([monkey.inspected for monkey in MONKEYS])[-2:]
    print(most_active[0] * most_active[1]) #part 1