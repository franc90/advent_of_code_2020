from collections import defaultdict

from advent_utils import assert_eq


def read_ints(numbers):
    return [int(number) for number in numbers.split(",")]


def part1(numbers, idx=2020):
    curr = -1
    nr_to_turns = defaultdict(list)
    for i, e in enumerate(numbers):
        curr = e
        nr_to_turns[e].append(i + 1)

    for i in range(len(numbers) + 1, idx + 1):
        if len(nr_to_turns[curr]) == 2:
            curr = nr_to_turns[curr][-1] - nr_to_turns[curr][-2]
        else:
            curr = 0
        nr_to_turns[curr].append(i)
        if len(nr_to_turns[curr]) > 2:
            del nr_to_turns[curr][0]

    return curr


assert_eq(436, part1(read_ints('0,3,6')))
assert_eq(1, part1(read_ints('1,3,2')))
assert_eq(10, part1(read_ints('2,1,3')))
assert_eq(27, part1(read_ints('1,2,3')))
assert_eq(78, part1(read_ints('2,3,1')))
assert_eq(438, part1(read_ints('3,2,1')))
assert_eq(1836, part1(read_ints('3,1,2')))
print(f"2020th nr = {part1(read_ints('15,12,0,14,3,1'))}")

assert_eq(175594, part1(read_ints('0,3,6'), 30000000))
assert_eq(2578, part1(read_ints('1,3,2'), 30000000))
assert_eq(3544142, part1(read_ints('2,1,3'), 30000000))
assert_eq(261214, part1(read_ints('1,2,3'), 30000000))
assert_eq(6895259, part1(read_ints('2,3,1'), 30000000))
assert_eq(18, part1(read_ints('3,2,1'), 30000000))
assert_eq(362, part1(read_ints('3,1,2'), 30000000))
print(f"30000000th nr = {part1(read_ints('15,12,0,14,3,1'), 30000000)}")
