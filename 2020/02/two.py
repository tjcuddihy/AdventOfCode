## Part 1
from dataclasses import dataclass, field

import re


@dataclass
class Password:
    """Class for keeping track of passwords."""

    entry: str
    data: str = field(init=False)
    range_low: str = field(init=False)
    range_high: str = field(init=False)
    letter: str = field(init=False)
    pwd: str = field(init=False)

    def __post_init__(self):
        p = re.compile("^(\d+)-(\d+) (\w): (\w+)$")
        self.data = p.match(
            self.entry,
        )
        self.range_low, self.range_high, self.letter, self.pwd = self.data.group(
            1, 2, 3, 4
        )
        self.range_low = int(self.range_low)
        self.range_high = int(self.range_high)

    def valid(self):
        n = len(re.findall(self.letter, self.pwd))
        return self.range_low <= n and n <= self.range_high

    def valid_part2(self):
        first = self.pwd[self.range_low - 1] == self.letter
        second = self.pwd[self.range_high - 1] == self.letter
        return first + second == 1


with open("two.txt", "r") as f:
    pwds = [Password(line) for line in f.read().splitlines()]


print(f"Part 1: {sum(x.valid() for x in pwds)}")
print(f"Part 2: {sum(x.valid_part2() for x in pwds)}")