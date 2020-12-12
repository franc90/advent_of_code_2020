from advent_utils import read_lines, assert_eq


def sum_taxi_distance(instructions):
    def find_dir(times, cur, reverse):
        possible_dirs = ['E', 'S', 'W', 'N']
        times = -times if reverse else times
        idx = (possible_dirs.index(cur) + times) % len(possible_dirs)
        return possible_dirs[idx]

    x, y, facing = 0, 0, 'E'
    for instr in instructions:
        val = int(instr[1:])
        if instr[0] == 'N' or (instr[0] == 'F' and facing == 'N'):
            y += val
        elif instr[0] == 'S' or (instr[0] == 'F' and facing == 'S'):
            y -= val
        elif instr[0] == 'W' or (instr[0] == 'F' and facing == 'W'):
            x -= val
        elif instr[0] == 'E' or (instr[0] == 'F' and facing == 'E'):
            x += val
        else:
            facing = find_dir(val // 90, facing, instr[0] == 'L')

    return abs(x) + abs(y)


def sum_taxi_distance2(instructions):
    def rotate(cnt):
        if cnt == 1:
            return wy, -wx
        elif cnt == 2:
            return -wx, -wy
        elif cnt == 3:
            return -wy, wx
        else:
            return wx, wy

    x, y, wx, wy = 0, 0, 10, 1
    for instr in instructions:
        val = int(instr[1:])
        if instr[0] == 'F':
            x += val * wx
            y += val * wy
        elif instr[0] == 'N':
            wy += val
        elif instr[0] == 'S':
            wy -= val
        elif instr[0] == 'W':
            wx -= val
        elif instr[0] == 'E':
            wx += val
        else:
            val = val // 90
            val = 4 - val if instr[0] == 'L' else val
            wx, wy = rotate(val)

    return abs(x) + abs(y)


assert_eq(25, sum_taxi_distance(read_lines('test')))
print(f"distance = {sum_taxi_distance(read_lines('input'))}")

assert_eq(286, sum_taxi_distance2(read_lines('test')))
print(f"distance = {sum_taxi_distance2(read_lines('input'))}")
