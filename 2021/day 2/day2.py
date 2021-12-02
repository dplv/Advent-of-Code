import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data =[i.split() for i in open(path + '\input.txt').read().split('\n')]

horizontal = sum([int(x[1]) for x in data if x[0] == 'forward'])
depth = sum([int(x[1]) for x in data if x[0] == 'down']) - sum([int(x[1]) for x in data if x[0] == 'up'])

result_p1 = horizontal * depth
print(result_p1)

horizontal = 0
depth = 0
aim = 0

for x in data:
    direction = x[0]
    value = int(x[1])

    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    else:
        horizontal += value
        depth += value * aim

result_p2 = horizontal * depth
print(result_p2)