import os
import math

dir = os.path.dirname(__file__)
motions = open(dir + '\input.txt', 'r').readlines()
motions = [motion.replace('\n', '').split() for motion in motions]

def dist_to_tail(head, tail):
    return abs(math.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2))

def best_tail_position():
    global HEAD
    global TAIL
    global DIRS

    dist = 2

    for dir in DIRS.values():
        t = (TAIL[0] + dir[0], TAIL[1] + dir[1])
        temp = dist_to_tail(HEAD, t)
        if temp < dist:
            dist = temp
            TAIL = t

    # if TAIL not in TAILS:
    TAILS.append(TAIL)
    return


DIRS = {
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
    'U': (0, 1)
}

HEAD = (0, 0)
TAIL = (0, 0)
    
TAILS = list()

# print(motions)

for motion in motions:
    print(f'== {motion[0]} {motion[1]} ==')
    dir = DIRS[motion[0]]
    dist = int(motion[1])
    for x in range(dist):
        HEAD = (HEAD[0] + 1 * dir[0], HEAD[1] + 1 * dir[1])
        if dist_to_tail(HEAD, TAIL) > 1:
            best_tail_position()   
        
        print(dir, x + 1, HEAD, TAIL, dist_to_tail(HEAD, TAIL))
    
print(TAILS, len(TAILS))