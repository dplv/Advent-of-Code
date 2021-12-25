import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

days = 256
fishes = [0 for x in range(9)]

for f in next(input).split(','):
    fishes[int(f)] += 1

for d in range(days):
    new = fishes.pop(0)
    fishes[6] += new
    fishes.append(new)

print(sum(fishes))