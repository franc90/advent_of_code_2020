from advent_utils import read_with_group_separator, flatten, assert_eq
from functools import reduce


def split_groups_into_letters(groups):
    def split_into_letters(group):
        return list(map(lambda i: list(i), group))

    return [split_into_letters(group) for group in groups]


def count_uniq_letters_in_groups(groups):
    return sum(map(lambda g: len(set(flatten(g))), groups))


def count_common_letters_in_groups(groups):
    def collect_common_letters_in_group(group):
        return reduce(lambda x, y: set(y).intersection(x), group)

    return sum(map(lambda g: len(collect_common_letters_in_group(g)), groups))


test = split_groups_into_letters(read_with_group_separator('test', '\n\n'))
assert_eq(11, count_uniq_letters_in_groups(test))
assert_eq(6, count_common_letters_in_groups(test))

text = read_with_group_separator('input', '\n\n')
groups_with_letters = split_groups_into_letters(text)
print(f"uniq:   {count_uniq_letters_in_groups(groups_with_letters)}")
print(f"common: {count_common_letters_in_groups(groups_with_letters)}")
