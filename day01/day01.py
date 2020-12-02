def readlines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def convert_to_ints(list_of_strigs):
    numbers = []
    for item in list_of_strigs:
        numbers.append(int(item))
    return numbers


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


values = convert_to_ints(readlines('input'))
print(get_first_two(values))
print(get_first_three(values))
