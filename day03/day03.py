from functools import reduce

from advent_utils import read_lines


def count_trees(lines, x, y, move_x, move_y):
    if y >= len(lines):
        return 0

    cur_line = lines[y]
    if x >= len(cur_line):
        x = x - len(cur_line)

    trees = count_trees(lines, x + move_x, y + move_y, move_x, move_y)
    if cur_line[x] == '#':
        trees += 1
    return trees


lines = read_lines('input')
tree_count = count_trees(lines, x=0, y=0, move_x=3, move_y=1)
print(f"{tree_count}")

paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_in_paths = map(lambda path: count_trees(lines, x=0, y=0, move_x=path[0], move_y=path[1]), paths)
val = reduce(lambda x, y: x * y, trees_in_paths)
print(val)
