from collections import defaultdict


def part_1(string, end=2020):
    numbers = [int(x) for x in string.split(",")]
    n = len(numbers)

    history = defaultdict(lambda: [0, 0, 0])  # 2nd last time, previous time, count

    prev = None

    for i, val in enumerate(numbers):
        # print(i, val)
        history[val][1] = i
        history[val][2] += 1
        # print(f"{history = }")
        prev = val

    for i in range(n, end):
        if i % 1000000 == 0:
            print(f"{i}, {i/end:.2%}")
        # for i in range(n, 10):
        # print(f"{prev = }")
        hist = history[prev]
        if hist[2] == 1:  # First time it was spoken
            val = 0
        else:  # Been said before
            val = hist[1] - hist[0]

        # print(i, val)
        prev = val
        history[val][0] = history[val][1]
        history[val][1] = i
        history[val][2] += 1
        # print(f"{history = }")
    # print(val)
    return val


assert part_1("0,3,6") == 436
assert part_1("1,3,2") == 1
assert part_1("2,1,3") == 10
assert part_1("3,1,2") == 1836

print(f"Part 1: {part_1('20,0,1,11,6,3')}")

print(f"Part 2: {part_1('20,0,1,11,6,3', 30000000)}")