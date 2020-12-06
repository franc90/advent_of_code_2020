from advent_utils import read_with_group_separator, flatten
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
uniq_letters = count_uniq_letters_in_groups(test)
common_letters = count_common_letters_in_groups(test)
assert 11 == uniq_letters, f"11 != {uniq_letters}"
assert 6 == common_letters, f"6 != {common_letters}"

text = read_with_group_separator('input', '\n\n')
groups_with_letters = split_groups_into_letters(text)
print(f"uniq:   {count_uniq_letters_in_groups(groups_with_letters)}")
print(f"common: {count_common_letters_in_groups(groups_with_letters)}")
