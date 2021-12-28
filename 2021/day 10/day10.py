import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

open_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_p2 = {')': 1, ']': 2, '}': 3, '>': 4}

illegal_list = []
incomplete_values = []
corrupted_list = []

lines = input.readlines()
lines = [line.replace('\n', '') for line in lines]

for line in lines:
    line = line.replace('\n', '')
    incomplete = True
    stack = []
    for c in line:
        if c in open_chars:
            stack.append(c)
        elif c in closing_chars:
            pos = closing_chars.index(c)
            if len(stack) > 0 and open_chars[pos] == stack[-1]:
                stack.pop()
            else:
                illegal_list.append(c)
                incomplete = False
                break
    
    if incomplete:
        incomplete_list = []
        for c in stack:
            pos = open_chars.index(c)
            incomplete_list.insert(0, closing_chars[pos])

        value = 0
        for c in incomplete_list:
            value *= 5
            value += points_p2[c]

        incomplete_values.append(value)

illegal_values = [points[c] for c in illegal_list]

#Part 1
print(sum(illegal_values))
    
#Part 2
incomplete_values.sort()
print(incomplete_values[int(len(incomplete_values)/2)])