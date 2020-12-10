def read_lines(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def read_with_group_separator(filename, separator):
    with open(filename, 'r') as f:
        groups = f.read().split(separator)
        return list(map(lambda g: g.split(), groups))


def read_list_of_ints(filename):
    return [int(line) for line in read_lines(filename)]


def flatten(a_list):
    return [item for sublist in a_list for item in sublist]


def assert_eq(expected, actual):
    assert expected == actual, f"{expected} != {actual}"
