from copy import deepcopy


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


def parse(s):
    op, val = s.split()
    val = int(val)
    return [op, val, False]


test_str = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

# data = filemap(parse, string=test_str)
# print(data)
data = filemap(parse, filename="eight.txt")

# Part 1
accumulator = 0
idx = 0
while True:
    inst = data[idx]
    if inst[2]:
        print(f"Part 1: {accumulator}")
        break
    else:
        inst[2] = True

    if inst[0] == "acc":
        accumulator += inst[1]
        idx += 1
    elif inst[0] == "jmp":
        idx += inst[1]
    else:
        idx += 1


# Part 2


def run(data_l):
    data_list = deepcopy(data_l)
    accumulator = 0
    idx = 0
    while True:
        if idx >= len(data_list):
            print(f"Part 2: {accumulator}")
            break

        inst = data_list[idx]
        if inst[2]:
            raise ValueError
        else:
            inst[2] = True

        if inst[0] == "acc":
            accumulator += inst[1]
            idx += 1
        elif inst[0] == "jmp":
            idx += inst[1]
        else:
            idx += 1


data = filemap(parse, string=test_str)
data = filemap(parse, filename="eight.txt")
for i, inst in enumerate(data):
    if inst[0] == "acc":
        continue
    temp = deepcopy(data)

    if temp[i][0] == "nop":
        temp[i][0] = "jmp"
    else:
        temp[i][0] = "nop"

    try:
        run(temp)
    except ValueError:
        continue
