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