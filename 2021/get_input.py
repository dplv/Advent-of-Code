import os

def GetInput(d):
    dir_path = os.path.realpath(__file__)
    path, filename = os.path.split(dir_path)                
    data = open(path + '\day ' + str(d) + '\input.txt').read().split('\n')

    return data


data = GetInput(1)
print(data)