import os
from collections import defaultdict

dir = os.path.dirname(__file__)
lines = open(dir + '\input.txt', 'r').readlines()
lines = [line.replace('\n', '') for line in lines]

tree = defaultdict(list)
sizes = defaultdict(int)
print(lines)

curr_dir = '/'

for line in lines:
    if line.startswith('$ cd ..'):
        new_dir = [i for i in tree if curr_dir in tree[i]]
        curr_dir = new_dir
    elif line.startswith('$ cd'):
        dir = line.replace('$ cd ', '')
        if dir.isalpha() or dir == '/':
            tree[dir] = []
            curr_dir = dir   
    elif not line.startswith('$'):
        tree[curr_dir].append(line)

def return_dir_size(dir: str) -> int:
    size = 0
    for element in tree[dir]:
        if element.startswith('dir'):
            element = element.replace('dir ', '')
            if element in sizes:
                size += sizes[element]
            else:
                size += return_dir_size(element)
        else:
            size += int(element.split(' ')[0])
    return size

print(tree)

for d in tree:
    sizes[d] = return_dir_size(d)

print(sum([val for val in sizes.values() if val <= 100000]))