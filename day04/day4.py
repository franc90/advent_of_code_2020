import re
from advent_utils import read_lines

required_fields = {
    "byr": "19[2-8][0-9]|199[0-9]|200[0-2]",
    "iyr": "201[0-9]|2020",
    "eyr": "202[0-9]|2030",
    "hgt": "(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in",
    "hcl": "\#[0-9a-f]{6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "\d{9}",
}


def parse_passports(lines):
    passports = []
    cur_passport = {}
    for line in lines:
        if line == "":
            passports.append(cur_passport)
            cur_passport = {}
        for elem in line.split(" "):
            pair = elem.split(":")
            if len(pair) == 2:
                cur_passport[pair[0]] = pair[1]
    passports.append(cur_passport)
    return passports


def has_all_required_fields(passport):
    for field in required_fields.keys():
        value = passport.get(field)
        if value is None:
            return False
        if re.fullmatch(required_fields[field], value) is None:
            # print(f"{value} does not match {required_fields[field]}")
            return False
    return True


def count_valid_passports(passports):
    return len(list(filter(lambda x: has_all_required_fields(x), passports)))


lines = read_lines('input')
passports = parse_passports(lines)
print(f"Total passports: {len(passports)}")
print(f"Valid passports: {count_valid_passports(passports)}")
