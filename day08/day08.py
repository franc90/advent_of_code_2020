from advent_utils import read_lines, assert_eq


def parse_program(lines):
    def parse_command(cmd):
        return cmd[0], int(cmd[1])

    return [parse_command(line.split()) for line in lines]


def compute(program):
    executed_lines = set()
    cmd_idx = 0
    acc = 0

    def exec_command(instr_nr):
        instr = program[instr_nr][0]
        arg = program[instr_nr][1]
        if instr == "nop":
            return instr_nr + 1, acc
        elif instr == "acc":
            return instr_nr + 1, acc + arg
        else:
            return instr_nr + arg, acc

    while cmd_idx < len(program):
        executed_lines.add(cmd_idx)
        next_cmd_idx, next_acc = exec_command(cmd_idx)
        if next_cmd_idx in executed_lines:
            break
        else:
            acc = next_acc
            cmd_idx = next_cmd_idx

    return cmd_idx, acc


def fix(program):
    def replace(prog, i):
        if prog[i][0] == "nop":
            prog[i] = "jmp", prog[i][1]
        elif prog[i][0] == "jmp":
            prog[i] = "nop", prog[i][1]

    for idx in range(len(program)):
        replace(program, idx)
        last_idx, acc = compute(program)
        if last_idx < len(program):
            replace(program, idx)
        else:
            return acc
    return None


test_program = parse_program(read_lines('test'))
assert_eq(5, compute(test_program)[1])
assert_eq(8, fix(test_program))

program = parse_program(read_lines('input'))
print(f"acc before loop starts: {compute(program)[1]}", )
print(f"acc after program fix: {fix(program)}", )
