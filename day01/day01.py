from advent_utils import read_lines


def convert_to_ints(list_of_strigs):
    return list(map(lambda s: int(s), list_of_strigs))


def get_first_two(ints):
    for x in range(0, len(ints) - 1):
        for y in range(x + 1, len(ints)):
            if ints[x] + ints[y] == 2020:
                return ints[x] * ints[y]


def get_first_three(ints):
    for x in range(0, len(ints) - 2):
        for y in range(x + 1, len(ints) - 1):
            for z in range(y + 1, len(ints)):
                if ints[x] + ints[y] + ints[z] == 2020:
                    return ints[x] * ints[y] * ints[z]


values = convert_to_ints(read_lines('input'))
print(get_first_two(values))
print(get_first_three(values))
