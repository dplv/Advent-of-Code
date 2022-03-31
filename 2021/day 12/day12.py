import os

dir_path = os.path.realpath(__file__)
path, filename = os.path.split(dir_path)
input = open(path + '\\test.txt')
lines = input.readlines()

graph = {}
paths = []

for line in lines:
    line = line.strip().split('-')
    u = line[0]
    v = line[1]

    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = []
        graph[u].append(v)

    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = []
        graph[v].append(u)

visitedList = []

def depthFirst(graph, currentVertex, visited, path):
    if currentVertex.islower():
        if currentVertex in visited:
            visited[currentVertex] += 1
        else:
            visited[currentVertex] = 1

    if currentVertex == 'end':
        path.append(currentVertex)
        visitedList.append(path)
        print(visited, max(visited.values()))
        return

    path.append(currentVertex)

    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy(), path.copy())

depthFirst(graph, 'start', {}, [])

# print(visitedList)
print(len(visitedList))