import time

from advent_utils import read_lines, assert_eq


def load(filename):
    lines = read_lines(filename)
    ints = list(map(lambda i: int(i), filter(lambda c: c != 'x', lines[1].split(','))))
    return int(lines[0]), ints


def part1(input):
    target, ints = input
    int_to_waittime = map(lambda i: (i, i - target % i), ints)
    id, wt = min(int_to_waittime, key=lambda t: t[1])
    return id * wt


def is_valid(elements, cur):
    return all((cur + e[0]) % e[1] == 0 for e in elements)


def part2(ids):
    st = time.time()
    elements = []
    for i, x in enumerate(ids.split(',')):
        if x == 'x':
            continue
        nr = int(x)
        elements.append((i, nr))

    max_elem = max(elements, key=lambda e: e[1])
    elements = list(map(lambda e: (e[0] - max_elem[0], e[1]), elements))

    cur = 0
    while not is_valid(elements, cur):
        cur += max_elem[1]

    et = time.time()
    print(f"{cur} in {(et - st)}")
    return cur + elements[0][0]


assert_eq(295, part1(load('test')))
print(f"waitime = {part1(load('input'))}")

assert_eq(1068781, part2('7,13,x,x,59,x,31,19'))
assert_eq(3417, part2('17,x,13,19'))
assert_eq(754018, part2('67,7,59,61'))
assert_eq(779210, part2('67,x,7,59,61'))
assert_eq(1261476, part2('67,7,x,59,61'))
assert_eq(1202161486, part2('1789,37,47,1889'))
print(
    f"timestamp = {part2('23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,13')}")
