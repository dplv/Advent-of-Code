import os
import math


def distance(knot_1: set, knot_2:set) -> float:
    return abs(math.sqrt((knot_1[0] - knot_2[0])**2 + (knot_1[1] - knot_2[1])**2))


def better_knot_position(knot_id: int, positions: list) -> set:
    global DIRS

    neighbor_position = positions[knot_id-1]
    position = positions[knot_id]
    dist = 2

    for dir in DIRS.values():
        new_position = (positions[knot_id][0] + dir[0], positions[knot_id][1] + dir[1])
        temp = distance(neighbor_position, new_position)
        if temp < dist:
            dist = temp
            position = new_position

    return position


def rope_motions(knots: int) -> int:
    global DIRS
    global MOTIONS

    start = (0, 0)
    knots_positions = list()
    knots_positions = [start] * knots
    
    tail_positions = list()
    tail_positions.append(start)

    for motion in MOTIONS:
        dir = DIRS[motion[0]]
        dist = int(motion[1])
        for _ in range(dist):
            head = knots_positions[0]
            head = (head[0] + 1 * dir[0], head[1] + 1 * dir[1])
            knots_positions[0] = head
            for k in range(1, knots):
                if distance(knots_positions[k-1], knots_positions[k]) >= 2:
                    knots_positions[k] = better_knot_position(k, knots_positions)

            if knots_positions[-1] not in tail_positions:
                tail_positions.append(knots_positions[-1])

    return len(tail_positions)


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    MOTIONS = open(dir + '\input.txt', 'r').readlines()
    MOTIONS = [motion.replace('\n', '').split() for motion in MOTIONS]

    DIRS = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0),
        'DR': (1, 1),
        'DL': (1, -1),
        'UR': (-1, 1 ),
        'UL': (-1, -1)
    }

    print(rope_motions(2)) #part 1
    print(rope_motions(10)) #part 2
