from collections import defaultdict
from math import prod


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


test_str_1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

test_str_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

test_data = filemap(parse, string=test_str_1)
# print(test_data)
data = filemap(parse, filename="ten.txt")


def part_1(data):
    dd = sorted(data)
    dd = [0] + dd + [max(dd) + 3]
    diffs = [dd[n] - dd[n - 1] for n in range(1, len(dd))]

    ones = sum(diff == 1 for diff in diffs)
    threes = sum(diff == 3 for diff in diffs)

    return ones * threes


print(f"Part 1 test: {part_1(test_data)}")
print(f"Part 1: {part_1(data)}")


def part_2(data):
    skip = False
    dd = list(reversed(sorted(data)))
    dd = [max(dd) + 3] + dd + [0]

    n = len(dd)
    print(f"{n = }")
    print(dd)

    alternatives = defaultdict(lambda: 1)
    for i, jolt in enumerate(dd):
        if skip:
            skip = False
            continue
        # print(i, jolt)
        for j in range(i + 2, i + 4):
            # print(j)

            if j >= n or (dd[i] - dd[j]) > 3:
                # print(dd[i], dd[j])
                break
            else:
                # print("success")
                alternatives[i] += 1
            if j - i > 2:
                skip = True

    return alternatives


part_2_res = part_2(test_data)

print(part_2_res)
print(sum(part_2_res.values()))
print(prod(part_2_res.values()))
# print(part_2_res.value())
# print(prod(part_2_res.values()) + part_2_res.values()[0])

# Had to look at : https://github.com/mattr555/advent-of-code/blob/master/2020/day10.py
# I had no idea how to solve this one.
data = set(data).union({0})
dp = [0] * (max(data) + 4)
dp[0] = 1
for i in range(len(dp)):
    dp[i] += dp[i - 1] if i - 1 in data else 0
    dp[i] += dp[i - 2] if i - 2 in data else 0
    dp[i] += dp[i - 3] if i - 3 in data else 0
print(dp[-1])