import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

lines = input.readlines()
lines = [list(line.replace('\n', '')) for line in lines]
line_len = len(lines[0])
lines.insert(0, [9 for x in range(line_len)])
lines.append([9 for x in range(line_len)])

#surrounding the matrix with 9 to avoid IndexError
for line in lines:
    line.insert(0, 9)
    line.append(9)

low_values = []
low_address = []

for r in range(1, len(lines) - 1):
    for c in range(1, len(lines[0]) - 1):
        r0 = lines[r-1][c]
        r1 = lines[r][c+1]
        r2 = lines[r+1][c]
        r3 = lines[r][c-1]

        adjacent = [int(x) for x in [r0, r1, r2, r3]]

        if int(lines[r][c]) < min(adjacent):
            low_values.append(int(lines[r][c]))
            low_address.append(str(r) + '-' + str(c))

#Part 1
print(sum(low_values) + len(low_values))

basins = []

#iterative depth-first search
for p in low_address:
    basin = []
    visited = set()
    visited.add(p)
    while visited:
        p = visited.pop()
        r = int(p.split('-')[0])
        c = int(p.split('-')[1])
        v = int(lines[r][c])
        if p not in basin and v != 9:
            basin.append(p)
            visited.add(str(r-1) + '-' + str(c))
            visited.add(str(r) + '-' + str(c+1))
            visited.add(str(r+1) + '-' + str(c))
            visited.add(str(r) + '-' + str(c-1))
        
    basins.append(len(basin))

result_p2 = 1
for n in sorted(basins, reverse=True)[:3]:
    result_p2 *= n

print(result_p2)