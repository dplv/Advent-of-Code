import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt', 'r')
lines = data.readlines()

count_part1, count_part2 = 0, 0

for line in lines:
    line = line.replace('\n', '').split(',')
    elf1, elf2 = [elf.split('-') for elf in line]
    elf1 = [int(x) for x in elf1]
    elf2 = [int(x) for x in elf2]

    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1] or elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        count_part1 += 1

    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1] or elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
        count_part2 += 1
        
print(count_part1)
print(count_part2)
