import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

lines = input.readlines()
lines = [list(line.replace('\n', '')) for line in lines]
lines = [[int(x) for x in line] for line in lines]

#surrounding the matrix with 0 to avoid IndexError
line_len = len(lines[0])
lines.insert(0, [0 for x in range(line_len)])
lines.append([0 for x in range(line_len)])
for line in lines:
    line.insert(0, 0)
    line.append(0)

adjacent_rows = (-1, 0, 1)
adjacent_cols = (-1, 0, 1)

steps = 250
flashes = 0
final_step = -1
flashes_sum = -1

# print(f'Step 0:')
# for line in lines:
#     print(0, line)

for step in range(steps):
    flashed = set()
    for i in range(1, len(lines) - 1): #rows
        for j in range(1, len(lines[0]) - 1): #cols
            to_flash = set()
            if (i, j) not in flashed:
                lines[i][j] += 1
            if lines[i][j] > 9:
                to_flash.add((i, j))
                while to_flash:
                    oct = to_flash.pop()
                    if oct not in flashed:
                        lines[oct[0]][oct[1]] = 0
                        for r in adjacent_rows:
                            for c in adjacent_cols:
                                if r != 0 or c != 0:
                                    if 0 < oct[0] + r <len(lines) - 1 and 0 < oct[1] + c < len(lines[0]) - 1:
                                        if (oct[0] + r, oct[1] + c) not in flashed:
                                            lines[oct[0] + r][oct[1] + c] += 1 
                                            if lines[oct[0] + r][oct[1] + c] > 9:
                                                to_flash.add((oct[0] + r, oct[1] + c))     
                        flashed.add(oct)
                        if step < 100:
                            flashes += 1
                            
    flashes_sum = sum([sum(line[1:-1]) for line in lines[1:-1]])

    if flashes_sum == 0:
        final_step = step
        break


#Part 1
print('p1:', 100, flashes)

#Part 2
print('p2:', final_step + 1)
