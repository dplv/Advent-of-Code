import os


def read_input():
    dir = os.path.dirname(__file__)
    lines = open(dir + '\input.txt', 'r').read().split('\n\n')
    lines = [line.split('\n') for line in lines if line != '']
    return lines


def compare_packets(pair: list) -> bool:
    left, right = [*pair]
    result = None

    if isinstance(left, int) and isinstance(right, int) and left != right:
        result = left < right
    
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if i > len(left) - 1:
                result = True
            elif i > len(right) - 1:
                result = False
            else:
                result = compare_packets([left[i], right[i]])
            
            if result is not None:
                return result

    elif isinstance(left, list) and not isinstance(right, list):
        result = compare_packets([left, [right]])
    
    elif not isinstance(left, list) and isinstance(right, list):
        result = compare_packets([[left], right])
    
    if result is not None:
        return result
        

def bubble_sort(l: list) -> list:
    for _ in range(len(l)):
        sorted = False
        for j in range(len(l)-1):
            if not compare_packets([l[j], l[j+1]]):
                l[j], l[j+1] = l[j+1], l[j]
                sorted = True
        if not sorted:
            break
    return l

if __name__ == '__main__':
    data = read_input()
    print(sum([i + 1 for i, pair in enumerate(data) if compare_packets([*map(eval, pair)])])) #part 1

    packets = [eval(packet) for pair in data for packet in pair] + [[[2]]] + [[[6]]]
    packets = bubble_sort(packets)
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)) #part 2
