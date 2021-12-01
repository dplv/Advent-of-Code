import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt').read().split('\n')

result_p1 = [int(i) - int(j) for i, j in zip(data[1:], data[:-1]) if int(i) - int(j) > 0]
print(len(result_p1))

sums = [int(i) + int(j) + int(k) for i, j, k in zip(data, data[1:], data[2:])]
result_p2 = [int(i) - int(j) for i, j in zip(sums[1:], sums[:-1]) if int(i) - int(j) > 0]
print(len(result_p2))