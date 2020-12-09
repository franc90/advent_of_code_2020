from advent_utils import read_lines, assert_eq
import itertools


def parse_input(lines):
    return [int(line) for line in lines]


def find_invalid_value(numbers, preamble_len):
    def is_valid(nr, preamble):
        pairs = itertools.combinations(preamble, 2)
        valid_pairs = list(filter(lambda pair: pair[0] + pair[1] == nr, pairs))
        return len(valid_pairs) > 0

    preamble_start = 0
    for idx in range(preamble_len, len(numbers)):
        if not is_valid(numbers[idx], numbers[preamble_start:preamble_start + preamble_len]):
            return numbers[idx]
        preamble_start += 1
    return None


def find_encryption_weakness(numbers, expected_sum):
    for sublist_len in range(2, len(numbers) - 1):
        for idx in range(len(numbers) - sublist_len + 1):
            sublist = numbers[idx:idx + sublist_len]
            if sum(sublist) == expected_sum:
                return min(sublist) + max(sublist)
    return None


test_numbers = parse_input(read_lines('test'))
invalid_test_value = find_invalid_value(test_numbers, preamble_len=5)
assert_eq(127, invalid_test_value)
assert_eq(62, find_encryption_weakness(test_numbers, invalid_test_value))

numbers = parse_input(read_lines('input'))
invalid_value = find_invalid_value(numbers, preamble_len=25)
print(f"invalid number: {invalid_value}")
print(f"encryption weakness: {find_encryption_weakness(numbers, invalid_value)}")
