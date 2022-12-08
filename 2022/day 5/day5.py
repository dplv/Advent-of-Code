import os

dir = os.path.dirname(__file__)
data = open(dir + '\input.txt', 'r').read().splitlines()

number_of_stacks = (len(data[0]) + 1) // 4
stacks = [list() for _ in range(number_of_stacks)]
stacks_p2 = [list() for _ in range(number_of_stacks)]
k, lines = 0, []

while data[k] != '':
    line = data[k]
    crates = [line[i] for i in range(1, len(line), 4)]
    for s, crate in enumerate(crates):
        if crate.isalpha():
            stacks[s].append(crate)
            stacks_p2[s].append(crate)
    k += 1

commands = [command.split(' ') for command in data[k+1:]] 
commands = [tuple(map(int, (c[1], c[3], c[5]))) for c in commands] #tuple(quantity, from, to)

for command in commands:
    for _ in range(command[0]):
        item = stacks[command[1] - 1].pop(0)
        stacks[command[2] - 1].insert(0, item)

message_9000 = ''.join([stack[0] for stack in stacks])
print(message_9000) #part1

for command in commands:
    for x in range(command[0] - 1, -1, -1):
        item = stacks_p2[command[1] - 1][x]
        stacks_p2[command[2] - 1].insert(0, item)
    stacks_p2[command[1] - 1] = stacks_p2[command[1] - 1][command[0]:]
        
message_9001 = ''.join([stack[0] for stack in stacks_p2])
print(message_9001) #part2
