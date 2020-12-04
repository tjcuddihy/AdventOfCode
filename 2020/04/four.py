from dataclasses import dataclass, field

import re


@dataclass
class Passport:
    """Class for keeping track of passwords."""

    entry: str

    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def __post_init__(self):
        for field in entry:
            key, val = field.split(":")
            setattr(self, key, val)

    def valid(self):
        return bool(
            self.byr
            and self.iyr
            and self.eyr
            and self.hgt
            and self.hcl
            and self.ecl
            and self.pid
        )

    def valid_part2(self):
        return (
            self.byr_is_valid()
            and self.iyr_is_valid()
            and self.eyr_is_valid()
            and self.hgt_val()
            and self.hcl_val()
            and self.ecl_val()
            and self.pid_val()
        )

    def pid_val(self):
        p = re.compile("^[0-9]{9}$")
        try:
            result = p.match(self.pid)
        except:
            return False
        if result:
            return True
        else:
            return False

    def ecl_val(self):
        valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl in valid

    def hcl_val(self):
        p = re.compile("^#[0-9a-f]{6}")
        try:
            result = p.match(self.hcl)
        except:
            return False
        if result:
            return True
        else:
            return False

    def hgt_val(self):
        p = re.compile("^(\d+)\s*(cm|in)")
        try:
            data = p.match(self.hgt)
            hgt = int(data[1])
            unit = data[2]
        except:
            return False

        if unit == "cm":
            return 150 <= hgt and 193 >= hgt
        elif unit == "in":
            return 59 <= hgt and 76 >= hgt
        else:
            print("Bad hgt")
            print(self)

    def eyr_is_valid(self):
        try:
            eyr = int(self.eyr)
        except:
            return False

        return 2020 <= eyr and 2030 >= eyr

    def iyr_is_valid(self):
        try:
            iyr = int(self.iyr)
        except:
            return False

        return 2010 <= iyr and 2020 >= iyr

    def byr_is_valid(self):
        try:
            byr = int(self.byr)
        except:
            return False

        return 1920 <= byr and 2002 >= byr


with open("four.txt", "r") as f:
    passports = []
    entry = []
    while True:
        line = f.readline()
        if not line:
            passports.append(Passport(entry))
            break
        elif line == "\n":
            passports.append(Passport(entry))
            entry = list()
        else:
            entry.extend(line.split())

print(f"N passports: {len(passports)}")
print(f"Part 1: {sum(x.valid() for x in passports)}")
print(f"Part 2: {sum(x.valid_part2() for x in passports)}")
