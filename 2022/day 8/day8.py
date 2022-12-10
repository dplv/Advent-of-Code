import os

dir = os.path.dirname(__file__)
forest = open(dir + '\input.txt', 'r').readlines()
forest = [list(map(int, [*line.replace('\n', '')])) for line in forest]

VISIBLE = set()

# print(forest)
def transp(m):
    result = []
    for _ in range(len(m)):
        result.append([0] * len(m[0]))
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result


def check_vis(forest):
    for i in range(len(forest)):
        for j in range(len(forest[0])):

            if (i, j) not in VISIBLE:
                if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
                    vis = True
                else:
                    tree = forest[i][j]
                    trees_left = tree > max(forest[i][:j])
                    trees_right = tree > max(forest[i][j+1:])

                    vis = any([trees_left, trees_right])

                if vis:
                    VISIBLE.add((i, j))

        # print(f'{i}-{j}: {forest[i][j]} {forest[i][:j]} {forest[i][j+1:]} {vis}')

def check_vis_tr(forest):
    for i in range(len(forest)):
        for j in range(len(forest[0])):

            if (j, i) not in VISIBLE:
                if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
                    vis = True
                else:
                    tree = forest[i][j]
                    trees_left = tree > max(forest[i][:j])
                    trees_right = tree > max(forest[i][j+1:])

                    vis = any([trees_left, trees_right])

                if vis:
                    VISIBLE.add((j, i))


# print(forest)
# print(transp(forest))

check_vis(forest)
check_vis_tr(transp(forest))
print(len(VISIBLE))

        

