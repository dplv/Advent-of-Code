import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt', 'r')
lines = data.readlines()

count_part1, count_part2 = 0, 0

for line in lines:
    line = line.replace('\n', '').split(',')
    elf1, elf2 = [elf.split('-') for elf in line]
    a, b = [int(x) for x in elf1]
    c, d = [int(x) for x in elf2]

    if a >= c and b <= d or c >= a and d <= b:
        count_part1 += 1

    if a >= c and a <= d or c >= a and c <= b:
        count_part2 += 1
        
print(count_part1)
print(count_part2)
