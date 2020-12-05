from math import ceil, floor

with open("five.txt", "r") as f:
    passes = [row.strip() for row in f.read().splitlines()]


def parse(code, dir_setter, start=0, end=127):
    if len(code) == 1:
        if code == dir_setter:
            return end
        else:
            return start
    mid_point = (start + end) / 2

    direction = code[0]
    code = code[1:]

    if direction == dir_setter:
        return parse(code, dir_setter, start=ceil(mid_point), end=end)
    else:
        return parse(code, dir_setter, start=start, end=floor(mid_point))


def calculate_part1(board):
    row = parse(board[:7], "B")
    seat = parse(board[7:], "R", 0, 7)
    return row * 8 + seat


def calculate_part2(board):
    row = parse(board[:7], "B")
    seat = parse(board[7:], "R", 0, 7)
    code = row * 8 + seat
    return (row, seat, code)


part_1 = [calculate_part1(x) for x in passes]
print(f"Part 1: {max(part_1)}")

part_2 = [calculate_part2(x) for x in passes]

d = dict()
for board in part_2:
    position = str(board[1]) + str(board[0])
    d[position] = board[2]

taken_seats = set(d.keys())
for row in range(128):
    for seat in range(8):
        position = str(seat) + str(row)
        if position in taken_seats:
            continue
        else:
            plus = str(seat) + str(row + 1)
            minus = str(seat) + str(row - 1)
            if plus not in taken_seats or minus not in taken_seats:
                continue
            else:
                print(f"Part 2: {row*8+seat}")
