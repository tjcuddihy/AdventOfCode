from math import prod
from functools import reduce


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


def parse(s):
    return s


def part_1(filename):
    with open(filename) as f:
        timestamp, busses = f.read().strip().split("\n")

    timestamp = int(timestamp)

    busses = [int(bus) for bus in busses.replace(",x", "").split(",")]

    mods = [int(timestamp) % int(bus) for bus in busses]
    waits = list(bus - wait for bus, wait in zip(busses, mods))
    wait = min(waits)
    next_bus = busses[waits.index(wait)]

    # return timestamp, busses, mods, next_bus, wait, next_bus * wait
    return next_bus * wait


data = part_1("thirteen.txt")
print(f"Part 1: {data}")


def part_2(filename):
    with open(filename) as f:
        _, busses = f.read().strip().split("\n")

    busses = [int(bus) for bus in busses.replace("x", "0").split(",")]
    positions = list(range(len(busses)))
    ignore = [positions[i] for i, x in enumerate(busses) if x == 0]
    for index in sorted(ignore, reverse=True):
        del busses[index]
        del positions[index]

    maximum = max(busses)
    idx_max = busses.index(maximum)
    quick_diff = positions[idx_max] - positions[0]

    m = prod(busses)

    return m - chinese_remainder(busses, positions)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


data = part_2("thirteen.txt")
print(f"Part 2: {data}")