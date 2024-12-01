import os
import re


def get_file() -> list:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(__location__ + os.sep + 'input.txt')
    data = file.read()
    file.close()
    lists = data.split('\n')
    list1 = list()
    list2 = list()
    for pair in lists:
        list1.append(int(pair.split('   ')[0]))
        list2.append(int(pair.split('   ')[1]))
    return (list1, list2)


if __name__ == '__main__':
    input = get_file()
    print(sum([e * input[1].count(e) for e in input[0]]))
