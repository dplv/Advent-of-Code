import os
from collections import defaultdict


def directory_size(dir: str) -> int:
    size = 0
    for element in tree[dir]:
        if element.startswith('dir'):
            element = element.replace('dir ', '')
            element = '/' + element if dir == '/' else dir + '/' + element
            if element in sizes:
                size += sizes[element]
            else:
                size += directory_size(element)
        else:
            size += int(element.split(' ')[0])
    return size


dir = os.path.dirname(__file__)
lines = open(dir + '\input.txt', 'r').readlines()
lines = [line.replace('\n', '') for line in lines]

tree = defaultdict(list)
sizes = defaultdict(int)
# print(lines)

path = ''

for line in lines:
    if line.startswith('$ cd ..'):
        path = path.rsplit("/", 1)[0]
    elif line.startswith('$ cd'):
        folder = line.replace('$ cd ', '')
        folder = '' if folder == '/' else folder
        path += '/' if path != '/' else ''
        path += folder
    elif not line.startswith('$'):
        tree[path].append(line)

for d in tree:
    sizes[d] = directory_size(d)

print(sum([size for size in sizes.values() if size <= 100000])) #part 1

MAX_SIZE = 70000000
REQUIRED = 30000000
USED     = sizes['/']
UNUSED   = MAX_SIZE - USED
MISSING  = REQUIRED - UNUSED

print(min([size for size in sizes.values() if size >= MISSING])) #part 2