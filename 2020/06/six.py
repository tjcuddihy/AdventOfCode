with open("six.txt", "r") as f:
    declarations = []
    entry = set()
    while True:
        line = f.readline()
        if not line:
            declarations.append(entry)
            break
        elif line == "\n":
            declarations.append(entry)
            entry = set()
        else:
            entry.update(line.strip())

print(f"Part 1: {sum(len(x) for x in declarations)}")


with open("six.txt", "r") as f:
    declarations = []
    entry = list()
    while True:
        line = f.readline()
        if not line:
            # declarations.append(entry)
            declarations.append(set.intersection(*entry))
            break
        elif line == "\n":
            declarations.append(set.intersection(*entry))
            entry = list()
        else:
            entry.append(set(line.strip()))

print(f"Part 2: {sum(len(x) for x in declarations)}")
