## Part 1
with open("one.txt", "r") as f:
    expenses = [int(_) for _ in f.read().splitlines()]


def finder(expenses):
    for i, expense in enumerate(expenses):
        for other in expenses[i + 1 :]:
            if expense + other == 2020:
                return (expense, other)


target = finder(expenses)
print(target)
print(f"Part 1: {target[0] * target[1]}")


## Part 2


def finder2(expenses):
    for i, first in enumerate(expenses):
        for j, second in enumerate(expenses[i + 1 :]):
            for k, third in enumerate(expenses[i + j + 1 :]):
                if first + second + third == 2020:
                    return (first, second, third)


target2 = finder2(expenses)
print(f"Part 2: {target2[0] * target2[1] * target2[2]}")