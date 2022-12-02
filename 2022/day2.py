import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt', 'r').read().split('\n')
data = list(map(str.split, data))

score = 0

for round in data:
    score += ['X', 'Y', 'Z'].index(round[1]) + 1
    if tuple(round) in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]: #win
        score += 6
    elif tuple(round) in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]: #draw
        score += 3

print(score) #part 1

score = 0

for round in data:
    if round[1] == 'Z': #win
        score += 6
        score += {'A': 2, 'B': 3, 'C': 1}[round[0]]
    elif round[1] == 'X': #lose
        score += {'A': 3, 'B': 1, 'C': 2}[round[0]]
    else:
        score += 3
        score += ['A', 'B', 'C'].index(round[0]) + 1

print(score) #part 2