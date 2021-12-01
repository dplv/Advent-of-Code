import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)                
data = open(path + '\input.txt').read().split('\n')

print(data)