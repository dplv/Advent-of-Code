import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

pos = [int(x) for x in next(input).split(',')]
pos.sort()

if len(pos) % 2 == 0:
    median = int((pos[int(len(pos)/2) - 1] + pos[int(len(pos)/2)])/2)
else:
    median = int(pos[len(pos)/2])

result_p1 = [abs(x - median) for x in pos]

print('p1:', sum(result_p1))

fuel = 99999999

for x in range(max(pos)):
    px = []
    for p in pos:
        #Part 1
        #px.append(abs(p-x))
        #Part 2
        px.append((abs(p-x)+1)/2*abs(p-x))
    fuel = int(sum(px)) if sum(px) < fuel else fuel

print('p2:', fuel)