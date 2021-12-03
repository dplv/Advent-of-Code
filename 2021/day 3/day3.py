import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
input = open(path + '\\input.txt').read()

data = input.replace('\n', '')
binary_len = len(input.split('\n')[0])
g_rate = []

for i in range(binary_len):
    if data[i:-1:binary_len].count('0') > data[i:-1:binary_len].count('1'):
        g_rate.append('0')
    else:
        g_rate.append('1')

e_rate = ['1' if i == '0' else '0' for i in g_rate]

g_rate_int = int(''.join(g_rate), 2)
e_rate_int = int(''.join(e_rate), 2)

result_p1 = g_rate_int * e_rate_int
print(result_p1)

o2_list = [list(e) for e in input.split()]
co2_list = o2_list

for i in range(binary_len):  
    data = []
    for j in o2_list:
        data.append(j[i])

    most_common = 0 if data.count('0') > data.count('1') else 1

    o2_list = [l for l in o2_list if int(l[i]) == most_common]

    if len(o2_list) == 1:
        break

o2 = int(''.join(o2_list[0]), 2)

for i in range(binary_len):  
    data = []
    for j in co2_list:
        data.append(j[i])

    less_common = 0 if data.count('0') <= data.count('1') else 1

    co2_list = [l for l in co2_list if int(l[i]) == less_common]

    if len(co2_list) == 1:
        break

co2 = int(''.join(co2_list[0]), 2)

result_p2 = o2*co2
print(result_p2)