from advent_utils import read_lines, assert_eq


def binary_search(line, start, end, lower_side_marker):
    for letter in line:
        if letter == lower_side_marker:
            end = (start + end) // 2 - 1
        else:
            start = (start + end) // 2 + 1
    return start


def decode_lines(lines):
    decoded = []
    for line in lines:
        row = binary_search(line[:8], 0, 127, "F")
        column = binary_search(line[7:], 0, 7, "L")
        seat_id = row * 8 + column
        decoded.append((line, row, column, seat_id))
    return decoded


def my_seat_id(decoded):
    seat_ids = list(map(lambda t: t[3], decoded))
    for x in range(0, len(seat_ids) - 1):
        if seat_ids[x] - seat_ids[x + 1] == 2:
            return seat_ids[x] - 1
    return -1


tests = [
    ("BFFFBBFRRR", 70, 7, 567),
    ("FFFBBBFRRR", 14, 7, 119),
    ("BBFFBBFRLL", 102, 4, 820),
]

for test in tests:
    assert_eq(test, decode_lines([test[0]])[0])

lines = read_lines('input')
decoded = decode_lines(lines)

decoded.sort(key=lambda t: t[3], reverse=True)
print(f"Max seat_id: {decoded[0][3]}")
print(f"My seat_id:  {my_seat_id(decoded)}")
