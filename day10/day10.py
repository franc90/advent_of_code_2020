from advent_utils import read_list_of_ints, assert_eq


def jolt_diffs(adapters):
    adapters = sorted(adapters)
    ones = 1 if min(adapters) == 1 else 0
    threes = 1
    for idx in range(len(adapters) - 1):
        diff = adapters[idx + 1] - adapters[idx]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    return ones * threes


def count_combinations(adapters):
    adapters = list(reversed(sorted(adapters)))
    adapters.append(0)

    combinations_per_adapter = {}
    for idx in range(1, len(adapters)):
        possible_next_adapters = filter(lambda x: adapters[idx] >= x - 3, adapters[:idx])
        count = sum(map(lambda x: combinations_per_adapter.get(x, 1), possible_next_adapters))
        combinations_per_adapter[adapters[idx]] = count
    return combinations_per_adapter[min(adapters)]


assert_eq(5 * 7, jolt_diffs(read_list_of_ints('test')))
assert_eq(22 * 10, jolt_diffs(read_list_of_ints('test2')))
print(f"jolt diff mult = {jolt_diffs(read_list_of_ints('input'))}")

assert_eq(8, count_combinations(read_list_of_ints('test')))
assert_eq(19208, count_combinations(read_list_of_ints('test2')))
print(f"adapter combinations = {count_combinations(read_list_of_ints('input'))}")
