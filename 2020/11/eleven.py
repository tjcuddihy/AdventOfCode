from copy import deepcopy
from itertools import product


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


def parse(s):
    return [x for x in s]


x_diff = [-1, 0, 1]
y_diff = [-1, 0, 1]
diff_set = set(product(x_diff, y_diff))
diff_set.remove((0, 0))
# print(diff_set)


def get_neighbours(i, j, seatmap):
    # n_row = len(seatmap)
    # n_col = len(seatmap[0])
    neighbours = []
    for combo in diff_set:
        try:
            row = i + combo[0]
            col = j + combo[1]
            if row < 0 or col < 0:
                continue
            neighbours.append(seatmap[i + combo[0]][j + combo[1]])
        except IndexError:
            continue
    return neighbours


def update_seat(i, j, seatmap, tolerance=4):
    curr_val = seatmap[i][j]
    neighbours = get_neighbours_2(i, j, seatmap)

    if curr_val == "L":
        if sum(x == "#" for x in neighbours) == 0:
            return "#"
        else:
            return "L"
    elif curr_val == "#":
        if sum(x == "#" for x in neighbours) >= tolerance:
            return "L"
        else:
            return "#"
    else:
        return curr_val


def part_1(filename):
    data = filemap(parse, filename)
    # print(get_neighbours(0, 0, data))
    old = deepcopy(data)
    new = deepcopy(data)
    while True:
        # for i in range(9):
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                new[i][j] = update_seat(i, j, old, 4)
        if old == new:
            print("Success")
            val = sum(x == "#" for row in old for x in row)
            # print(val)
            # print(old)
            return val
        else:
            old = deepcopy(new)


# assert part_1("eleven_test.txt") == 37
# print(part_1("eleven.txt"))


def search_direction(i, j, seatmap, direction):
    to_search = direction
    while True:
        row = i + to_search[0]
        col = j + to_search[1]
        if row < 0 or col < 0:
            return None
        try:
            if seatmap[row][col] == ".":
                to_search = tuple(sum(x) for x in zip(to_search, direction))
                continue
            else:
                return seatmap[i + to_search[0]][j + to_search[1]]
        except IndexError:
            return None


def get_neighbours_2(i, j, seatmap):
    neighbours = []
    for combo in diff_set:
        neighbour = search_direction(i, j, seatmap, combo)
        if neighbour:
            neighbours.append(neighbour)
    return neighbours


test = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "L", ".", "L", ".", "#", ".", "#", ".", "#", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]
print(get_neighbours(1, 1, test))

data = filemap(parse, "eleven_test2.txt")
print(get_neighbours(3, 3, data))


def part_2(filename):
    data = filemap(parse, filename)
    old = deepcopy(data)
    new = deepcopy(data)
    while True:
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                new[i][j] = update_seat(i, j, old, 5)
        if old == new:
            print("Success")
            val = sum(x == "#" for row in old for x in row)
            print(val)
            # print(old)
            return val
        else:
            old = deepcopy(new)


assert part_2("eleven_test.txt") == 26
print(part_2("eleven.txt"))