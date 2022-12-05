import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt', 'r').read().split('\n')
# data = list(map(str.split, data))

def priority(c: str) -> int:
    return '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)

score = 0

for rucksack in data:
    size = len(rucksack) // 2
    score += priority([c for c in rucksack[0:size] if c in rucksack[size:]][0])

print(score) #part 1

g = 0
score = 0

while g <= len(data) - 2:
    c = [c for c in set(''.join(data[g:g + 3])) if c in data[g] and c in data[g+1] and c in data[g+2]][0]
    score += priority(c)
    g += 3

print(score) #part 2