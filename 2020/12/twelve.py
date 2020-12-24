from dataclasses import dataclass
import numpy as np


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
    data = filemap(parse, filename=filename)
    ship = Ship()
    for instr in data:
        ship.update(instr)
    return ship.location()


@dataclass
class Ship:
    easting: float = 0.0
    northing: float = 0.0
    heading: float = 0.0

    def move(self, x):
        if self.heading == 0:
            self.easting += x
        elif self.heading == 90:
            self.northing -= x
        elif self.heading == 180:
            self.easting -= x
        elif self.heading == 270:
            self.northing += x

    def rotate(self, direction, amount):
        if direction == "R":
            self.heading = (self.heading + amount) % 360
        else:
            self.heading = (self.heading - amount) % 360

    def update(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action == "N":
            self.northing += value
        elif action == "E":
            self.easting += value
        elif action == "S":
            self.northing -= value
        elif action == "W":
            self.easting -= value
        elif action in ["L", "R"]:
            self.rotate(action, value)
        elif action == "F":
            self.move(value)
        else:
            raise IndexError("Broken")

    def location(self):
        return (self.northing, self.easting)


print(part_1("twelve_test.txt"))

print(f"Part 1 test: {sum(abs(x) for x in part_1('twelve_test.txt'))}")
print(f"Part 1: {sum(abs(x) for x in part_1('twelve.txt'))}")


@dataclass
class Waypoint:
    northing: int = 1
    easting: int = 10
    rotations = {
        90: np.array([[0, -1], [1, 0]]),
        180: np.array([[-1, 0], [0, -1]]),
        270: np.array([[0, 1], [-1, 0]]),
    }

    def rotate(self, direction, degrees):
        if direction == "R":
            if degrees == 90:
                degrees = 270
            elif degrees == 270:
                degrees = 90

        rotation = np.dot([self.northing, self.easting], self.rotations[degrees])
        self.northing, self.easting = rotation


@dataclass
class Ship2:
    easting: float = 0.0
    northing: float = 0.0
    heading: float = 0.0
    waypoint: Waypoint = Waypoint()

    def move(self, x):

        move_north = self.waypoint.northing * x
        if self.waypoint.northing < 0 and move_north > 0:
            move_north *= -1
        move_east = self.waypoint.easting * x
        if self.waypoint.easting < 0 and move_east > 0:
            move_east *= -1

        self.northing += move_north
        self.easting += move_east

    def update(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action == "N":
            self.waypoint.northing += value
        elif action == "E":
            self.waypoint.easting += value
        elif action == "S":
            self.waypoint.northing -= value
        elif action == "W":
            self.waypoint.easting -= value
        elif action in ["L", "R"]:
            self.waypoint.rotate(action, value)
        elif action == "F":
            self.move(value)
        else:
            raise IndexError("Broken")

    def location(self):
        return (self.northing, self.easting)


def part_2(filename):
    data = filemap(parse, filename=filename)
    ship = Ship2(waypoint=Waypoint())
    for instr in data:
        ship.update(instr)
    return ship.location()


print(part_2("twelve_test.txt"))

print(f"Part 2 test: {sum(abs(x) for x in part_2('twelve_test.txt'))}")
print(f"Part 2: {sum(abs(x) for x in part_2('twelve.txt'))}")