import os
import math


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    return data.split('\n')


def get_hand_strength(hand: tuple[str, str], order: list) -> int:
    cards, _ = hand
    type = [cards.count(s) for s in set(cards)]

    if len(type) == 1:
        x = 700
    elif max(type) == 4:
        x = 600
    elif len(type) == 2:
        x = 500
    elif len(type) == 3 and max(type) == 3:
        x = 400
    elif len(type) == 3 and max(type) == 2:
        x = 300
    elif len(type) == 4 and max(type) == 2:
        x = 200
    elif len(type) == 5:
        x = 100

    return [x] + [order.index(s) for s in cards]


def part1(data: list) -> (int, int):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    hands = [tuple(d.split()) for d in data]
    hands = sorted(hands, key = lambda x: get_hand_strength(x, order))
    return sum([int(hand[1]) * (rank + 1) for rank, hand in enumerate(hands)])


def part2(data: list) -> (int, int):
    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    hands = [d.split() for d in data]

    for i, hand in enumerate(hands):
        if hand[0].find('J') > -1:
            strength = 0
            for card in order[1:]:
                temp_hand = hand[0].replace('J', card)
                strength = max(strength, get_hand_strength((temp_hand, hand[1]), order)[0])
            true_strength = get_hand_strength(hand, order)
            final_strength = [strength] + true_strength[1:]
        else:
            final_strength = get_hand_strength(hand, order)
        hands[i] = (hand[0], hand[1], final_strength)

    hands = sorted(hands, key = lambda x: x[2])
    return sum([int(hand[1]) * (rank + 1) for rank, hand in enumerate(hands)])


if __name__ == '__main__':
    input = get_file()

    print(part1(input))
    print(part2(input))
