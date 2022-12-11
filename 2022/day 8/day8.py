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
    global FOREST
    check_trees(FOREST)
    check_trees(transpose(FOREST), True)
    return len(VISIBLE_TREES)


def prod(l: list) -> int:
    result = 1
    for i in l:
        result *= i
    return result


def count_visible_trees(tree, trees):
    count = 0
    for t in trees:
        if t < tree:
            count += 1
        else:
            count += 1
            break
    return count


def scores(f, transposed = False):
    global SCORES
    for i in range(len(f)):
        for j in range(len(f[0])):
            if i == 0 or j == 0 or i == len(f) - 1 or j == len(f[0]) - 1:
                score = 0
            else:
                tree = f[i][j]
                # if (i, j) == (3, 2) or (transposed and (i, j) == (2, 3)):
                #     print(i, j)
                trees_left = f[i][:j][::-1]
                trees_right = f[i][j+1:]

                score_left = count_visible_trees(tree, trees_left)
                score_right = count_visible_trees(tree, trees_right)

                if transposed:
                    SCORES[(j, i)].append(score_left)
                    SCORES[(j, i)].append(score_right)
                else:
                    SCORES[(i, j)].append(score_left)
                    SCORES[(i, j)].append(score_right)
    return


def best_view():
    global SCORES
    global FOREST
    scores(FOREST)
    scores(transpose(FOREST), True)
    return max([prod(x) for x in SCORES.values()])


if __name__ == '__main__':
    VISIBLE_TREES = set()
    SCORES = defaultdict(list)
    FOREST = read_input()

    print(all_visible_trees()) #part 1
    print(best_view()) #part 2
