import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def get_hand_strength(hand: tuple[str, str]) -> int:
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cards, bin = hand
    type = [cards.count(s) for s in set(cards)]
    value = sum([order.index(s) for s in cards])
    if len(type) == 1:
        return 7 * 1000 + value
    elif max(type) == 4:
        return 6 * 1000 + value
    elif len(type) == 2:
        return 5 * 1000 + value
    elif len(type) == 3 and max(type) == 3:
        return 4 * 1000 + value
    elif len(type) == 3 and max(type) == 2:
        return 3 * 1000 + value
    elif len(type) == 4 and max(type) == 2:
        return 2 * 1000 + value
    elif len(type) == 5:
        return 1 * 1000 + value


def solution(data: list) -> (int, int):
    hands = [tuple(d.split()) for d in data]
    print(hands)
    for h in hands:
        print(h, get_hand_strength(h))
    print('-' * 15)
    hands = sorted(hands, key = lambda x: get_hand_strength(x))
    for h in hands:
        print(h, get_hand_strength(h))
    # print([get_hand_strength(h) for h in hands])
    # hands = hands.sort(key=get_hand_strength)
    return


if __name__ == '__main__':
    input = get_file()

    print(solution(input))
