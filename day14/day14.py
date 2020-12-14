from advent_utils import read_lines, assert_eq


def convert(nr, mask):
    new_nr = [0] * 36
    for i in range(36):
        if mask[i] == '1':
            new_nr[i] = 1
        elif mask[i] != '0' and 36 - len(nr) <= i:
            new_nr[i] = nr[i - (36 - len(nr))]
    return int("".join([str(i) for i in new_nr]), 2)


def part1(lines: list):
    mask, numbers = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {}
    for line in lines:
        if "mask = " in line:
            mask = line[7:]
        else:
            line = line.replace("mem[", "").replace("] = ", ",").split(",")
            numbers[line[0]] = convert([int(x) for x in bin(int(line[1]))[2:]], mask)

    return sum(numbers.values())


def convert2(nr, mask):
    addresses = [[0] * 36]
    for i in range(36):
        additional_addr = []
        for addr in addresses:
            if mask[i] == '1':
                addr[i] = 1
            elif mask[i] == '0':
                if 36 - len(nr) <= i:
                    addr[i] = nr[i - (36 - len(nr))]
            else:
                addr_copy = addr.copy()
                addr[i] = '1'
                addr_copy[i] = '0'
                additional_addr.append(addr_copy)
        addresses.extend(additional_addr)

    return list(map(lambda l: int("".join([str(i) for i in l]), 2), addresses))


def part2(lines: list):
    mask, numbers = "000000000000000000000000000000000000", {}
    for line in lines:
        if "mask = " in line:
            mask = line[7:]
        else:
            line = line.replace("mem[", "").replace("] = ", ",").split(",")
            for idx in convert2([int(x) for x in bin(int(line[0]))[2:]], mask):
                numbers[idx] = int(line[1])

    return sum(numbers.values())


assert_eq(165, part1(read_lines('test')))
print(f"sum = {part1(read_lines('input'))}")

assert_eq(208, part2(read_lines('test2')))
print(f"sum = {part2(read_lines('input'))}")
