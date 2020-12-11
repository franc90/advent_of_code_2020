from advent_utils import read_matrix, flatten, assert_eq


def count_neighbors_p1(src, i, j):
    cnt = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0 or x >= len(src) or y >= len(src[i]):
                continue
            if src[x][y] == '#':
                cnt += 1
    return cnt


def count_neighbors_p2(src, i, j):
    def count(a, b):
        if 0 <= a < len(src) and 0 <= b < len(src[0]) and src[a][b] == '#':
            return 1
        else:
            return 0

    def check_done(a, b):
        if a < 0 or b < 0 or a >= len(src) or b >= len(src[0]):
            return True
        elif src[a][b] == 'L':
            return True
        elif src[a][b] == '#':
            return True
        else:
            return False

    cnt = 0
    for x in reversed(range(0, i)):
        if check_done(x, j):
            cnt += count(x, j)
            break
    for x in range(i + 1, len(src)):
        if check_done(x, j):
            cnt += count(x, j)
            break
    for y in reversed(range(0, j)):
        if check_done(i, y):
            cnt += count(i, y)
            break
    for y in range(j + 1, len(src)):
        if check_done(i, y):
            cnt += count(i, y)
            break
    for x in reversed(range(0, i)):
        if check_done(x, j - (i - x)):
            cnt += count(x, j - (i - x))
            break
    for x in range(i + 1, len(src)):
        if check_done(x, j + (x - i)):
            cnt += count(x, j + (x - i))
            break
    for x in reversed(range(0, i)):
        if check_done(x, j + (i - x)):
            cnt += count(x, j + (i - x))
            break
    for x in range(i + 1, len(src)):
        if check_done(x, j - (x - i)):
            cnt += count(x, j - (x - i))
            break
    return cnt


def count_occupied(counter, src, cpy, round=0, tolerance=4):
    def transform():
        for i in range(len(src)):
            for j in range(len(src[i])):
                if src[i][j] == '#' and counter(src, i, j) >= tolerance:
                    cpy[i][j] = 'L'
                elif src[i][j] == 'L' and counter(src, i, j) == 0:
                    cpy[i][j] = '#'
                else:
                    cpy[i][j] = src[i][j]

    def count_taken():
        return len(list(filter(lambda e: e == '#', flatten(cpy))))

    transform()
    if src == cpy:
        return count_taken()
    else:
        return count_occupied(counter, cpy, src, round + 1, tolerance)


def count_p1(m1):
    m2 = [line.copy() for line in m1]
    return count_occupied(count_neighbors_p1, m1, m2)


def count_p2(m1):
    m2 = [line.copy() for line in m1]
    return count_occupied(count_neighbors_p2, m1, m2, tolerance=5)


assert_eq(37, count_p1(read_matrix('test')))
print(f"occupied = {count_p1(read_matrix('input'))}")

assert_eq(26, count_p2(read_matrix('test')))
print(f"occupied = {count_p2(read_matrix('input'))}")
