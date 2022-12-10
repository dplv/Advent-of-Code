import os
from collections import defaultdict


def read_input():
    dir = os.path.dirname(__file__)
    data = open(dir + '\input.txt', 'r').readlines()
    return [list(map(int, [*line.replace('\n', '')])) for line in data]


def transpose(matrix: list) -> list:
    transposed = []
    for _ in range(len(matrix)):
        transposed.append([0] * len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


def check_trees(forest, transposed = False):
    global VISIBLE_TREES
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if (i, j) not in VISIBLE_TREES or (transposed and (j, i) not in VISIBLE_TREES):
                if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
                    visible = True
                else:
                    tree = forest[i][j]
                    trees_left = tree > max(forest[i][:j])
                    trees_right = tree > max(forest[i][j+1:])
                    visible = any([trees_left, trees_right])

                if visible:
                    if transposed:
                        VISIBLE_TREES.add((j, i))
                    else:
                        VISIBLE_TREES.add((i, j))
    return


def all_visible_trees():
    global VISIBLE_TREES
    forest = read_input()
    check_trees(forest)
    check_trees(transpose(forest), True)
    return len(VISIBLE_TREES)


if __name__ == '__main__':
    # VISIBLE_TREES = set()
    # print(all_visible_trees())

    forest = read_input()

    SCORES = defaultdict(list)

    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
                score = 0
            else:
                tree = forest[i][j]
                trees_left = forest[i][:j][::-1]
                score_left = len([i for i, v in enumerate(trees_left) if v >= tree])
                if score_left == 0:
                    score_left = len(trees_left)
                else:
                    score_left += 1 if score_left < len(trees_left) else 0
                trees_right = forest[i][j+1:]
                score_right = len([i for i, v in enumerate(trees_right) if v >= tree])
                if score_right == 0:
                    score_right = len(trees_left)
                else:
                    score_right += 1 if score_right < len(trees_right) else 0

                SCORES[(i,j)].append(score_left)
                SCORES[(i,j)].append(score_right)

    print(forest)
    forest = transpose(forest)

    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
                score = 0
            else:
                tree = forest[i][j]
                trees_left = forest[i][:j][::-1]
                score_left = len([i for i, v in enumerate(trees_left) if v >= tree])
                if score_left == 0:
                    score_left = len(trees_left)
                else:
                    score_left += 1 if score_left < len(trees_left) else 0
                trees_right = forest[i][j+1:]
                score_right = len([i for i, v in enumerate(trees_right) if v >= tree])
                if score_right == 0:
                    score_right = len(trees_left)
                else:
                    score_right += 1 if score_right < len(trees_right) else 0

                SCORES[(j,i)].append(score_left)
                SCORES[(j,i)].append(score_right)




    print(SCORES)