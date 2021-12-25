import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

# format x1,y1 -> x2,y2
lines = input.readlines()
lines = [line.replace('\n', '').split(' -> ') for line in lines]

grid_size = max(
    [max(
        int(vector[0].split(',')[0]),
        int(vector[0].split(',')[1]),
        int(vector[1].split(',')[0]),
        int(vector[1].split(',')[1])
    ) for vector in lines]
)

grid = [[0 for x in range(grid_size + 1)] for y in range(grid_size + 1)]

for vector in lines:
    x1 = int(vector[0].split(',')[0])
    y1 = int(vector[0].split(',')[1])
    x2 = int(vector[1].split(',')[0])
    y2 = int(vector[1].split(',')[1])

    if x1 == x2:
        for y in range(min(y1, y2), max(y1 + 1, y2 + 1)):
            grid[x1][y] += 1          
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1 + 1, x2 + 1)):
            grid[x][y1] += 1
    #Part 2
    else:
        x_dir = 1 if x2 > x1 else -1
        y_dir = 1 if y2 > y1 else -1
        for p in range(abs(x1 - x2) + 1):
            grid[x1][y1] += 1
            x1 += x_dir
            y1 += y_dir

result = sum([sum([1 for x in l if x > 1]) for l in grid])
print(result)