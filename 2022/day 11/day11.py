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
    ROUNDS = 20 

    mod_factor = math.prod([monkey.test for monkey in MONKEYS])
    for round in range(ROUNDS):
        if round % 1000 == 0:
            print(round)
        for m in MONKEYS:
            # print(m.id, m.test, m.test_true, type(m.test_true))
            for item in m.items:
                m.inspected += 1
                worry_level = eval(f'{item} {m.operation}')
                worry_level %= mod_factor
                # worry_level = worry_level // 3
                if worry_level % m.test == 0:
                    MONKEYS[m.test_true].items.append(worry_level)
                else:
                    MONKEYS[m.test_false].items.append(worry_level)

                # print(m.id, item, '|', eval(f'{item} {m.operation}'))
            m.items.clear()

    for m in MONKEYS:
        print(f'Monkey {m.id}: {m.items} {m.inspected}')

    most_active = sorted([m.inspected for m in MONKEYS])[-2:]
    print(most_active[0] * most_active[1]) #part 1