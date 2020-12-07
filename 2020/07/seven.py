from dataclasses import dataclass, field
import re
from string import punctuation, digits


def filemap(func, filename=None, string=None, sep="\n"):
    if string:
        raw = string
    else:
        with open(filename) as f:
            raw = f.read()
    raw = raw.strip().split(sep)
    return list(map(func, raw))


@dataclass
class Bag:

    entry: str
    descr: str = field(init=False)
    qty: int = 0

    def __post_init__(self):
        strings = self.entry.translate(str.maketrans("", "", punctuation)).split()
        if strings[0] in digits:
            self.qty = int(strings.pop(0))
        self.descr = " ".join(strings[:2])


def parse(s):
    bag, contains = s.split("contain")
    bag = bag.strip().removesuffix("s")
    bag = Bag(bag)

    contains = list(map(Bag, contains.strip().split(", ")))

    contains = {x.descr: x for x in contains}

    return bag, contains


test_str = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data = filemap(parse, filename="seven.txt", sep="\n")
# data = filemap(parse, string=test_str, sep="\n")

part_1 = dict()

for bag in data:
    for k, v in bag[1].items():
        if k not in part_1.keys():
            part_1[k] = set()
        part_1[k].add(bag[0].descr)

part_1_res = set()
search = part_1["shiny gold"]

while search:
    candidate = search.pop()
    part_1_res.add(candidate)
    try:
        search.update(part_1[candidate])
    except KeyError:
        continue

print(f"Part 1: {len(part_1_res)}")

# PArt 2
test_str = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

# data = filemap(parse, string=test_str, sep="\n")

part_2 = dict()
for bag in data:
    part_2[bag[0].descr] = {sub.descr: sub.qty for sub in bag[1].values()}


def rec(bag):
    if bag == "no other":
        return 0

    else:
        return sum(qty + rec(new_bag) * qty for new_bag, qty in part_2[bag].items())


print(f"Part 2: {rec('shiny gold')}")
