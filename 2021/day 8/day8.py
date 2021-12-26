import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\input.txt')

"""
Segments
 00
1  2
 33
4  5
 66
"""

display = {
    '012456': 0,
    '25': 1,
    '02346': 2,
    '02356': 3,
    '1235': 4,
    '01356': 5,
    '013456': 6,
    '025': 7,
    '0123456': 8,
    '012356': 9
}

values = []

segments = input.readlines()
segments_p1 = [s.split(' | ')[1].replace('\n', '') for s in segments]
segments_p1 = [s.split() for s in segments_p1]
segments_p1 = [[len(e) for e in s] for s in segments_p1]
segments_p1 = sum([sum([1 for e in s if e in (2, 3, 4, 7)]) for s in segments_p1])

print('p1:', segments_p1)

lines = [line.replace('\n', '') for line in segments]

for line in lines:
    segments = ['x' for i in range(7)]
    code, output = line.split(' | ')
    output = output.split()
    code = code.split()
    code = sorted(code, key=len)
    n1 = code[0]
    segments[2] = n1[0] #temp
    segments[5] = n1[1] #temp
    n7 = code[1]
    n4 = code[2]
    n8 = code[9]
    segments[0] = list(set(n7).difference(set(n1)))[0] #perm

    #n3
    for c in code:
        if len(c) == 5 and all(e in c for e in segments if e != 'x' ):
            n3 = c
            segments[3] = list(set(c).difference(set(n7)))[0] #temp
            segments[6] = list(set(c).difference(set(n7)))[1] #temp

    #n9
    for c in code:
        if len(c) == 6 and all(e in c for e in segments if e != 'x'):
            n9 = c
            segments[1] = list(set(c).difference(set(n3)))[0] #perm

    #n0
    for c in code:
        if len(c) == 6 and sum([1 for e in c if e in segments]) == 5 and all(e in c for e in segments[2] + segments[5]):
            n0 = c
            segments[4] = list(set(c).difference(set(n9)))[0] #perm
            if segments[3] in c:
                s = segments[3]
                segments[3] = segments[6]
                segments[6] = s

    #n6
    for c in code:
        if len(c) == 6 and sum([1 for e in c if e in segments[2] + segments[5]]) == 1:
            n6 = c
            if segments[2] in c:
                s = segments[2]
                segments[2] = segments[5]
                segments[5] = s

    number = ''
    for n in output:
        render = ''
        for c in n:
            render += str(segments.index(c))
            render = ''.join(sorted(render))
        number += str(display[render])

    values.append(int(number))

print('p2:', sum(values))