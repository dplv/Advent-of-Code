import os

dir = os.path.dirname(__file__)
buffer = open(dir + '\input.txt', 'r').read()

# m = 4 #part 1
m = 14 #part 2

for x in range(m, len(buffer) + 1):
    marker = buffer[x-m:x]
    if len(set(marker)) == m:
        print(x)
        break