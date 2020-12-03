import re
from operator import xor


def readlines(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def is_password_valid_old(line):
    m = re.search('(\d+)-(\d+) (\w+): (\w+)', line)
    min_repeats = int(m.group(1))
    max_repeats = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    repeats = password.count(char)
    # print(f"{password}: {char} {min_repeats}<={repeats}<={max_repeats}")
    return min_repeats <= repeats <= max_repeats


def is_password_valid_new(line):
    m = re.search('(\d+)-(\d+) (\w+): (\w+)', line)
    first_pos = int(m.group(1))
    last_pos = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    # print(f"{password}: {char} {min_repeats}<={repeats}<={max_repeats}")
    return xor((password[first_pos-1] == char), (password[last_pos-1] == char))


passwords = readlines('input')
passwords_old = list(filter(lambda x: is_password_valid_old(x), passwords))
passwords_new = list(filter(lambda x: is_password_valid_new(x), passwords))
print(f"valid passwords by old rules: {len(passwords_old)}")
print(f"valid passwords by old rules: {len(passwords_new)}")
