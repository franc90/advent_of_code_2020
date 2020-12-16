from advent_utils import assert_eq, flatten


def read_with_group_separator(filename):
    with open(filename, 'r') as f:
        return f.read().split("\n\n")


def parse_rules(lines):
    lines = list(map(lambda l: l.split(":"), lines))
    rules = {}
    for line in lines:
        ranges = line[1].split("or")
        ranges = list(map(lambda r: r.split("-"), ranges))
        ranges = list(map(lambda r: range(int(r[0]), int(r[1]) + 1), ranges))
        rules[line[0]] = ranges
    return rules


def split(filename):
    groups = read_with_group_separator(filename)
    predicates = parse_rules(groups[0].split("\n"))
    my_ticket = [int(field) for field in groups[1].split("\n")[1].split(",")]
    nearby_tickets = []
    for line in groups[2].split("\n")[1:]:
        # print(line)
        nearby_tickets.append([int(field) for field in line.split(",")])
    return predicates, my_ticket, nearby_tickets


def is_invalid(n, rules: dict):
    for k in rules.keys():
        if any([n in r for r in rules[k]]):
            return False
    return True


def find_invalid_nearby_values(rules: dict, numbers):
    invalid_nrs = list(filter(lambda n: is_invalid(n, rules), flatten(numbers)))
    return invalid_nrs


def filter_out_invalid(rules: dict, numbers: list):
    return list(filter(lambda n: not any([is_invalid(x, rules) for x in n]), numbers))


def part1(filename):
    rules, _, nearby = split(filename)
    return sum(find_invalid_nearby_values(rules, nearby))


def part2(filename):
    rules, my_ticket, nearby = split(filename)
    nearby = filter_out_invalid(rules, nearby)

    names = [list(rules.keys()) for _ in range(len(nearby[0]))]
    for ticket in nearby:
        for idx in range(len(ticket)):
            invalid_names = []
            for possible_name in names[idx]:
                if not any([ticket[idx] in r for r in rules[possible_name]]):
                    invalid_names.append(possible_name)
            for n in invalid_names:
                names[idx].remove(n)

    name_assignment = []
    while len(names) > 0:
        name_assignment.extend(flatten(list(filter(lambda l: len(l) == 1, names))))
        new_names = []
        for n in names:
            new_n = []
            for v in n:
                if v not in name_assignment:
                    new_n.append(v)
            if len(new_n) > 0:
                new_names.append(new_n)
        names = new_names

    count = 1
    for i, a in enumerate(name_assignment):
        if "departure " in a:
            print(f"  '{a}' is my_ticket[{i}]={my_ticket[i]}")
            count *= my_ticket[i]

    return count


assert_eq(71, part1("test"))
print(f"sum of invalid = {part1('input')}")
print(f"sum of departures = {part2('input')}")
