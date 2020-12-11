import itertools


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


def parse(s):
    return int(s)


test_str = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

test_data = filemap(parse, string=test_str)
# print(test_data)
data = filemap(parse, filename="nine.txt")


def search(data, preamble_length):
    idx = preamble_length

    while True:
        candidates = data[idx - preamble_length : idx]
        val = data[idx]

        if not any(
            sum(candidate) == val for candidate in itertools.permutations(candidates, 2)
        ):
            return val
        idx += 1


print(f"Part 1 test: {search(test_data, 5)}")
print(f"Part 1: {search(data, 25)}")


def crack(data, target):
    data_len = len(data)

    start = 0

    while True:
        for i in range(start + 2, data_len):
            if sum(data[start:i]) == target:
                vals = data[start:i]
                return (min(vals), max(vals))
            elif sum(data[start:i]) > target:
                start += 1
                break
            else:
                continue


print(f"Part 2 test: {sum(crack(test_data, search(test_data, 5)))}")
print(f"Part 2: {sum(crack(data, search(data, 25)))}")