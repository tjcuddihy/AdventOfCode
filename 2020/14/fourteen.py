import re
from collections import defaultdict
from itertools import product
import copy

MEMORY_ADDR_RE = re.compile("mem\[(\d+)\]")


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


def parse(s):
    return s.split(" = ")


def part_1(filename):
    data = filemap(parse, filename)
    mem_map = defaultdict(lambda: 0)

    while data:
        mask = data.pop(0)
        assert mask[0] == "mask", "uhoh?!"
        ops = []
        while data:
            if data[0][0] == "mask":
                break
            else:
                ops.append(data.pop(0))
        mask = mask[1]  # Keep the actual mask

        mask_and = int(f"0b{mask.replace('X', '1')}", 2)
        mask_or = int(f"0b{mask.replace('X', '0')}", 2)

        for op in ops:
            binary = int(op[1])  # bin(int(op[1]))
            address = int(MEMORY_ADDR_RE.match(op[0])[1])
            new = binary & mask_and
            new = new | mask_or
            mem_map[address] = new

    return mem_map.values()


assert sum(part_1("fourteen_test.txt")) == 165

data = part_1("fourteen.txt")
print(f"Part 1: {sum(data)}")


def part_2(filename):
    data = filemap(parse, filename)
    mem_map = defaultdict(lambda: 0)

    while data:
        mask = data.pop(0)
        assert mask[0] == "mask", "uhoh?!"
        ops = []
        while data:
            if data[0][0] == "mask":
                break
            else:
                ops.append(data.pop(0))
        mask = mask[1]  # Keep the actual mask

        for op in ops:
            address = int(MEMORY_ADDR_RE.match(op[0])[1])
            value = int(op[1])
            mem_map = operate(address, value, mask, mem_map)

    return mem_map.values()


def operate(address, value, mask, mem_map):
    address_binary = f"{address:036b}"

    working_addr = [x for x in address_binary]
    for i, char in enumerate(mask):
        if char == "0":
            continue
        elif char == "1":
            working_addr[i] = "1"
        else:  # X
            working_addr[i] = "X"

    addresses = generate_address_combinations("".join(working_addr))
    for addr in addresses:
        mem_map[int(addr, 2)] = value

    return mem_map


def generate_address_combinations(address_string):

    options = [(c,) if c != "X" else ("0", "1") for c in address_string]
    return list(("".join(o) for o in product(*options)))


assert sum(part_2("fourteen_test_2.txt")) == 208
data = part_2("fourteen.txt")
print(f"Part 2: {sum(data)}")