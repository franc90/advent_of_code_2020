def read_lines(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def read_with_group_separator(filename, separator):
    with open(filename, 'r') as f:
        groups = f.read().split(separator)
        return list(map(lambda g: g.split(), groups))


def flatten(a_list):
    return [item for sublist in a_list for item in sublist]
