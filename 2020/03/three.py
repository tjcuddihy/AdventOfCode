with open("three.txt", "r") as f:
    slope_map = [line.rstrip() for line in f]

N_ROWS = len(slope_map)
N_COLS = len(slope_map[0])


def send_it_bro(i, j):
    """
    i = n rows to drop
    j = n cols to drop
    """
    row_inc = 0
    col_inc = 0
    n_trees = 0

    while True:
        col = col_inc % N_COLS
        try:
            if slope_map[row_inc][col] == "#":
                n_trees += 1
        except IndexError:
            print(row_inc, col_inc, n_trees, col)
            raise

        row_inc += i
        col_inc += j

        if row_inc >= N_ROWS:
            break
    return n_trees


a = send_it_bro(1, 1)
b = send_it_bro(1, 3)
c = send_it_bro(1, 5)
d = send_it_bro(1, 7)
e = send_it_bro(2, 1)

print(f"Part 1: {b}")
print(f"Part 2: {a * b * c * d * e}")
