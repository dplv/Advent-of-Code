import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt', 'r')
lines = data.readlines()

calories = list()
temp = 0

for line in lines:
    if line == '\n':
        calories.append(temp)
        temp = 0    
    else:
        temp += int(line.replace('\n', ''))

calories.sort(reverse=True)

print(calories[0])          #part 1
print(sum(calories[0:3]))   #part 2